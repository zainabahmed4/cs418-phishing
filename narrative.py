"""Reproduce the README narrative from the checked-in PhiUSIIL CSV.

Run python narrative.py with pandas, numpy, and matplotlib installed.
Intervals are approximate 95% intervals clustered by the recorded Domain.
"""

from pathlib import Path
from typing import NamedTuple

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "datasets" / "PhiUSIIL_Phishing_URL_Dataset.csv"
FIGURES = ROOT / "figures"
COLORS = {"Phishing": "#9e421e", "Legitimate": "#285e81"}


class Estimate(NamedTuple):
    value: float
    low: float
    high: float


def interval(value, contributions):
    """Compute a normal interval from domain-level influence contributions."""
    domains = len(contributions)
    se = np.sqrt(domains / (domains - 1) * np.square(contributions).sum())
    return Estimate(*(100 * x for x in (value, value - 1.96 * se, value + 1.96 * se)))


def compare(data, event):
    """Return within-label shares and the phishing-minus-legitimate gap."""
    totals = (
        data.assign(event=event)
        .groupby(["Domain", "label"])["event"]
        .agg(["sum", "size"])
        .unstack(fill_value=0)
    )
    estimates = {}
    influences = {}
    rates = {}
    for label, name in [(0, "Phishing"), (1, "Legitimate")]:
        hits = totals["sum"][label]
        rows = totals["size"][label]
        rate = hits.sum() / rows.sum()
        influence = (hits - rate * rows) / rows.sum()
        rates[name] = rate
        influences[name] = influence
        estimates[name] = interval(rate, influence)
        result = estimates[name]
        # An empirical cluster interval degenerates when all outcomes match.
        precision = (
            f" (95% CI {result.low:.2f} to {result.high:.2f}%)"
            if result.low != result.high
            else " (all rows had the same outcome)"
        )
        print(f"  {name}: {hits.sum():,}/{rows.sum():,} = {result.value:.2f}%{precision}")

    gap = interval(
        rates["Phishing"] - rates["Legitimate"],
        influences["Phishing"] - influences["Legitimate"],
    )
    print(f"  Gap: {gap.value:+.2f} pp (95% CI {gap.low:+.2f} to {gap.high:+.2f} pp)")
    return estimates


def report(name, data, event):
    print(name)
    return compare(data, event)


def draw(filename, title, subtitle, axis_label, rows, maximum):
    """Plot shares on a common percentage scale within each figure."""
    plt.rcParams["font.family"] = "DejaVu Sans"
    fig, ax = plt.subplots(figsize=(9, 2.7 + 0.69 * len(rows)), facecolor="white")
    fig.subplots_adjust(left=0.28, right=0.95, bottom=0.23, top=0.72)
    fig.text(0.05, 0.91, title, fontsize=17, weight="bold", color="#192b39")
    fig.text(0.05, 0.81, subtitle, fontsize=10.5, color="#405563")
    for index, (row_label, estimates) in enumerate(rows):
        for name, offset in [("Phishing", -0.18), ("Legitimate", 0.18)]:
            estimate = estimates[name]
            ax.errorbar(
                estimate.value,
                index + offset,
                xerr=[[estimate.value - estimate.low], [estimate.high - estimate.value]],
                fmt="o",
                color=COLORS[name],
                markersize=6,
                capsize=3 if estimate.low != estimate.high else 0,
                zorder=3,
                clip_on=False,
                label=name if index == 0 else None,
            )
            ax.annotate(
                f"{estimate.value:.1f}%",
                (estimate.high, index + offset),
                xytext=(9, 0),
                textcoords="offset points",
                ha="left",
                va="center",
                color=COLORS[name],
                fontsize=10,
                weight="bold",
            )
    ax.set_xlim(0, maximum)
    ax.set_ylim(len(rows) - 0.5, -0.5)
    ax.set_yticks(range(len(rows)), [row[0] for row in rows])
    ax.set_xticks(np.arange(0, maximum, 20))
    ax.xaxis.set_major_formatter("{x:.0f}%")
    ax.set_xlabel(axis_label, labelpad=8, color="#405563")
    ax.grid(axis="x", color="#dce4e8")
    ax.tick_params(axis="both", length=0, pad=8, labelcolor="#405563")
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.legend(loc="lower left", bbox_to_anchor=(0.04, 0.02), ncol=2, frameon=False)
    fig.text(
        0.95, 0.055, "Whiskers show domain-clustered 95% intervals where estimable.",
        ha="right", fontsize=8.5, color="#405563",
    )
    fig.savefig(FIGURES / filename, dpi=160)
    plt.close(fig)


def main():
    fields = ["URL", "Domain", "URLLength", "IsHTTPS", "LineOfCode", "HasPasswordField", "label"]
    data = pd.read_csv(DATA, usecols=fields, keep_default_na=False)
    data["scheme_https"] = data["URL"].str.lower().str.startswith("https://")
    data["text_length"] = data["URL"].str.len()
    unique_urls = data.drop_duplicates("URL")
    https = data.loc[data["scheme_https"]]

    print(f"PhiUSIIL: {len(data):,} rows, {data['Domain'].nunique():,} recorded domains")
    disagreement = data["scheme_https"] != data["IsHTTPS"].eq(1)
    print(f"HTTPS field/scheme disagreements: {disagreement.sum():,}")
    print(f"Repeated URL rows removed in sensitivity check: {len(data) - len(unique_urls):,}")
    scheme = report("HTTPS from URL text", data, data["scheme_https"])
    stored = report("HTTPS from stored field", data, data["IsHTTPS"].eq(1))
    report("HTTPS from URL text, one row per exact URL", unique_urls, unique_urls["scheme_https"])

    length_results = []
    for field, description in [("text_length", "URL text"), ("URLLength", "Stored length")]:
        medians = https.groupby("label")[field].median()
        threshold = medians.loc[1]
        print(f"HTTPS {description} medians: phishing {medians.loc[0]:g}, legitimate {threshold:g}")
        result = report(f"HTTPS, {description} ≤ {threshold:g}", https, https[field] <= threshold)
        length_results.append((f"{description}\n≤ {threshold:g} characters", result))

    report("Password field, all rows", data, data["HasPasswordField"].eq(1))
    password_https = report("Password field, HTTPS only", https, https["HasPasswordField"].eq(1))
    medium = https.loc[https["LineOfCode"].between(100, 999)]
    password_medium = report("Password field, HTTPS with 100–999 lines", medium, medium["HasPasswordField"].eq(1))
    large = https.loc[https["LineOfCode"] >= 1000]
    password_large = report("Password field, HTTPS with 1,000+ lines", large, large["HasPasswordField"].eq(1))
    small_counts = https.loc[https["LineOfCode"] < 100, "label"].value_counts()
    print(f"HTTPS under 100 lines: {small_counts.get(0, 0):,} phishing, {small_counts.get(1, 0):,} legitimate")

    FIGURES.mkdir(exist_ok=True)
    draw(
        "https-overlap.png",
        "Nearly half of phishing URLs use HTTPS",
        "PhiUSIIL • Two ways to measure HTTPS in the same records",
        "Share using HTTPS within each label",
        [("URL text", scheme), ("Stored HTTPS field", stored)],
        115,
    )
    draw(
        "short-https-urls.png",
        "Some phishing URLs are both HTTPS and short",
        "PhiUSIIL • Short means at or below the legitimate HTTPS median for each measure",
        "Share at or below the length threshold within each label",
        length_results,
        66,
    )
    draw(
        "password-field-by-page-size.png",
        "The password-field pattern reverses within page-size groups",
        "PhiUSIIL • HTTPS pages grouped by lines of code",
        "Share with a password field within each label",
        [
            ("All HTTPS pages", password_https),
            ("100–999 lines", password_medium),
            ("1,000+ lines", password_large),
        ],
        74,
    )


if __name__ == "__main__":
    main()
