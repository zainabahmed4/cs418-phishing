# PhiUSIIL: Individual Exploratory Data Analysis

Source notebook: [notebooks/eda_phiusiil.ipynb](notebooks/eda_phiusiil.ipynb). This contribution covers only the primary PhiUSIIL dataset; it does not combine the group's datasets or replace the final report.

## 1. Dataset profile

The CSV has **235,795 rows and 56 columns**, with each row representing a URL and its webpage. There are five text columns, 41 integer columns, and ten floating-point columns. `FILENAME` identifies records, and `label` gives the classification. The [UCI documentation](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset) confirms **0 = phishing** and **1 = legitimate**, matching the project README.

There are **100,945 phishing rows (42.8%)** and **134,850 legitimate rows (57.2%)**. No column has null values. The class comparison plots use percentages within each class because the legitimate class is larger. The sample's class balance is not an estimate of phishing prevalence on the internet.

See notebook Section A, including **“Class distribution in PhiUSIIL”**, the schema, null counts, and descriptive statistics.

## 2. Anomalies and decisions

The original CSV was not modified. No observations were removed or source features overwritten. Counts can overlap and should not be added together.

| Finding | Affected rows | Decision and reason |
|---|---:|---|
| Repeated URLs | 850 across 425 URLs; 425 extra occurrences | Kept and flagged. Filenames are unique, the rows are not identical, and repeated URL labels agree. Collection times are unavailable. |
| Stored URL length differs from displayed URL text | 187,151 | Kept and flagged. 187,149 are shorter by one character, one by four, and one by 35. Possible preprocessing differences need verification. |
| HTTPS feature disagrees with URL scheme | 493 | Kept and flagged. All are phishing rows with HTTP text but `IsHTTPS = 1`; the extraction context is unknown. |
| Possible title encoding damage | 8 | Left flagged. A pattern screen finds common encoding artifacts, not confirmed corrupt titles; automatic text repair could change meaning. |
| Leading/trailing title whitespace | 1 | Left flagged because title text is not used in the plots. |
| Title `0` with `HasTitle = 0` | 32,714 | Kept as an absence marker rather than treated as an ordinary title or null. |
| Title `0` with `HasTitle = 1` | 5 | Left flagged; a literal title is possible. |
| Title `na` with `HasTitle = 1` | 5 | Left flagged as ambiguous text rather than automatically marked missing. |
| Stored URL length above pooled 99th percentile, 144 | 2,350 | Kept. These are tail observations, not confirmed errors. |
| Lines of code above pooled 99th percentile, 10,388 | 2,357 | Kept and shown on a log scale; large webpages are possible. |

The basic checks found **zero** nulls, blank text values, exact duplicate rows, unexpected binary codes, negative numeric values, nonfinite floats, out-of-range ratios or scores, and URL parsing failures. Domain and TLD lengths match their strings; no checked URL character count exceeds its stored URL length. Numeric types are suitable for the analysis. The range checks do not fully validate the original feature extractor.

The maximum `LargestLineLength` is 13,975,732. A large minified line is possible, so this value alone does not justify removing a row. Two URLs contain uppercase characters; paths can be case sensitive, so they were retained without normalization.

Sensitivity checks preserve the main patterns:

- Calculated text-length medians are **34 for phishing and 27 for legitimate**, compared with stored medians of **34 and 26**.
- Phishing HTTPS usage is **49.22%** using the supplied indicator and **48.74%** using the URL scheme. Both give 100% for legitimate rows.
- Keeping the first occurrence of each URL gives 100,520 phishing and 134,850 legitimate URLs. Phishing HTTPS usage is **49.12%**, password fields **5.33%**, and external form submission **0.43%**, close to the full-data results.

See notebook Section B for the computed checks, length offsets, and sensitivity tables. The main analysis retains all original rows.

## 3. Important feature distributions

The notebook includes four distribution figures in Section C, covering eleven selected features:

| Plot title | Main finding |
|---|---|
| **Stored URL length distribution / Domain length distribution** | Stored URL length has median 27, middle half 23–34, and maximum 6,097. Domain length has median 20, middle half 16–24, and maximum 110. URL length has a much longer right tail. |
| **Distribution of recorded subdomain counts** | One subdomain is the most common value: 178,406 rows (75.7%). Both quartiles and the median are 1, with a maximum of 10. |
| **Frequency of selected URL and webpage indicators** | HTTPS is present in 78.26%; obfuscation in 0.21%; IP domains in 0.27%; recorded URL redirects in 13.34%; password fields in 10.23%; and external form submission in 4.40%. |
| **Special-character ratio distribution / Webpage lines of code distribution** | The special-character ratio has median 0.05, middle half 0.038–0.083, and maximum 0.397. Lines of code have median 429, middle half 18–1,277, and maximum 442,666. |

Log axes show the full URL-length and page-size ranges. Those histograms show counts in unequal-width bins, not density per character or line. `NoOfURLRedirect` only takes 0 and 1, so it is plotted as an indicator. The supplied subdomain count is retained without assuming that counting dots reproduces the feature.

## 4. Relationship findings and interpretation

See notebook Section D for three relationship figures. Percentages below mean feature prevalence **within each classification**, not the probability of phishing given a feature.

### URL and domain lengths by classification

Plots: **“Stored URL length by classification”** and **“Domain length by classification.”**

| Measure | Phishing | Legitimate |
|---|---:|---:|
| Median stored URL length | 34 | 26 |
| URL length middle half | 26–48 | 23–29 |
| Mean stored URL length | 45.72 | 26.23 |
| Maximum stored URL length | 6,097 | 57 |
| Median domain length | 22 | 19 |
| Domain length middle half | 16–29 | 16–22 |

**So what?** Phishing URLs tend to be longer and more variable, as expected, but the ranges overlap. Short URLs do not establish legitimacy. This agrees with the teammate's existing URL-length result and extends it to domain length. Boxplot outlier markers are hidden for readability; all rows remain in the calculations and full ranges appear elsewhere in the notebook.

**What next?** Compare URL length within domain-length ranges to separate hostname differences from paths and queries. Check computed text lengths before choosing cutoffs.

### Recorded subdomain counts by classification

Plot: **“Recorded subdomain counts by classification.”**

One subdomain occurs in **63.0% of phishing rows versus 85.2% of legitimate rows**. Three or more occur in **5.3% versus 1.3%**. All **13,983** zero-subdomain rows are phishing. However, mean counts are nearly equal: **1.169 versus 1.162**.

**So what?** Averages hide the different category distributions. More subdomains are somewhat associated with phishing here, but the zero-count group is also distinct. This may partly reflect collection or counting conventions rather than a universal phishing rule. The CSV does not show whether people notice these differences.

**What next?** Confirm the counting rule, inspect zero-count examples, and compare subdomain groups within HTTPS and domain-length categories.

### URL and webpage indicators by classification

Plot: **“URL and webpage indicators by classification.”**

| Feature present | Phishing rows | Legitimate rows |
|---|---:|---:|
| HTTPS | 49.22% | 100.00% |
| Obfuscation | 0.48% | 0.00% |
| IP domain | 0.63% | 0.00% |
| Recorded URL redirect | 15.17% | 11.98% |
| Password field | 5.39% | 13.85% |
| External form submission | 0.43% | 7.37% |

Recorded redirects show a smaller difference between classes; their binary encoding does not describe chain length.

**So what?** Nearly half of phishing rows have HTTPS, so this cue alone cannot identify legitimacy. Obfuscation and IP domains appear only in phishing rows but cover very few phishing examples. Surprisingly, password fields and external form submission are more common in legitimate rows. Legitimate sites use forms too, so these features are not automatic warning signs.

Page size may matter: the median `LineOfCode` is **12 for phishing versus 1,105 for legitimate**. Collection or extraction differences could contribute to the form patterns. The associations do not show causation or how people recognize phishing.

**What next?** Compare form features among HTTPS-only rows and within page-size groups. A later class activity could test recognition of visible HTTPS cues while controlling other characteristics.

## 5. Research question reflection and follow-up

**Original research question:** Which features of phishing links and webpages make them harder for people to recognize?

A question this dataset can address more directly is:

**Which URL and webpage characteristics differ between phishing and legitimate rows in PhiUSIIL, especially when phishing rows also have HTTPS or ordinary-looking domain structures?**

Many phishing rows share technical characteristics with legitimate rows, including HTTPS, one recorded subdomain, and overlapping URL lengths. These are useful starting points for selecting examples. They do not prove that people are fooled by any particular feature: the dataset has no participant responses, recognition scores, or measures of what people saw.

The proposed class activity could compare recognition accuracy for phishing examples with and without visible HTTPS cues or different URL structures, using otherwise comparable examples. Webpage appearance would require screenshots or a controlled presentation, since extracted source-code features are not necessarily visible to participants.

Before group integration, useful follow-ups are to verify extraction conventions, compare combinations within HTTPS and page-size subgroups, and check whether teammates' datasets show similar patterns. Source selection, repeated URLs, and feature inconsistencies limit generalization. Cross-dataset comparisons and the unified report remain outside this individual contribution.
