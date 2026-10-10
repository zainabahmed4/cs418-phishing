# PhiUSIIL: Individual Exploratory Data Analysis

This analysis looks at the primary PhiUSIIL dataset using [notebooks/eda_phiusiil.ipynb](notebooks/eda_phiusiil.ipynb). It focuses on the dataset's main patterns and how they relate to our research question. The group comparisons and final report will build on this work.

## 1. Dataset Profile

The dataset contains **235,795 rows and 56 columns**. Each row represents a URL and its webpage, with features describing things like URL length, HTTPS use, and webpage forms. `FILENAME` identifies each record, while `label` tells us whether it is phishing or legitimate. According to the [UCI documentation](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset), **0 means phishing and 1 means legitimate**.

About **43% of the rows are phishing and 57% are legitimate**, so there are more legitimate examples. I used percentages within each class when comparing them so that the larger class would not dominate the plots. These percentages describe this dataset; they do not tell us how common phishing is across the internet.

There are no missing values. The columns include text, whole numbers, and decimal values, and the numeric types were suitable for the analysis.

*Source: notebook Section A, including the class distribution plot and basic dataset checks.*

## 2. Data Anomalies

I checked for missing values, duplicates, unusual feature values, and differences between the URL text and the recorded features. I kept all original rows because the unusual values were not clearly errors. The main findings are listed below. Some rows appear in more than one check, so the counts should not be added together.

| Finding | Rows affected | Action taken |
|---|---:|---|
| Repeated URLs | 850 rows across 425 URLs | Kept and flagged. The rows are not identical, and the labels agree for each repeated URL. |
| Recorded URL length differs from the URL text | 187,151 | Kept and flagged. Almost all differences are just one character, which may come from preprocessing. |
| HTTPS feature disagrees with the URL text | 493 | Kept and flagged. These are phishing rows whose URLs start with HTTP but have `IsHTTPS = 1`. |
| Possible title encoding issues | 8 | Flagged for review because the text may contain encoding artifacts. |
| Extra whitespace around a title | 1 | Left flagged. Title text was not used in the plots. |
| Title is `0` and `HasTitle = 0` | 32,714 | Treated as a marker for no title. |
| Title is `0` or `na` and `HasTitle = 1` | 10 | Left flagged because it is unclear whether these are actual titles or missing-value markers. |
| URL length above the 99th percentile | 2,350 | Kept because a long URL is not necessarily an error. |
| Webpage lines of code above the 99th percentile | 2,357 | Kept and plotted on a log scale so large values would fit. |

The other basic checks did not find blank text values, exact duplicate rows, unexpected binary values, negative numbers, invalid numeric values, or URL parsing failures. The checked ratios and scores were within their expected ranges. Domain and TLD lengths matched their text, and the checked URL character counts did not exceed the recorded URL length.

A few values still need care. For example, the largest recorded line length was around 14 million characters. This could be a long minified line of code, so I did not remove it based on size alone. I also kept the two URLs with uppercase characters because changing the case of a URL path can change where it leads.

To see whether the inconsistencies affected the results, I compared recorded URL lengths with lengths calculated from the text, checked HTTPS using the URL scheme, and repeated some comparisons using one row per URL. The main patterns stayed similar. For example, phishing URLs were still generally longer, and roughly half of the phishing rows still used HTTPS.

These checks support keeping the original data for this analysis, but they do not fully confirm how the features were extracted.

*Source: notebook Section B, including the anomaly checks and comparisons using alternative measurements.*

## 3. Feature Distributions

The distribution plots showed a few clear patterns:

- **URL and domain length:** Most URLs and domains were fairly short, but URL length had a much wider range. A small number of very long URLs stretched the distribution to the right.
- **Subdomain count:** One recorded subdomain was by far the most common value, appearing in about three quarters of the rows.
- **URL and webpage indicators:** HTTPS was common overall. Obfuscation and IP-based domains were rare, while redirects and password fields appeared more often. External form submission was less common.
- **Special-character ratio:** Most URLs had a relatively low proportion of special characters.
- **Webpage size:** The number of lines of code varied widely. Many pages were small, but some were much larger.

I used log scales for URL length and webpage size to show their full ranges. The histogram bars show row counts, and the bins on these scales have different widths. The redirect feature only contains 0 and 1, so I treated it as an indicator of whether a redirect was recorded. I also used the supplied subdomain count without assuming it could be recreated just by counting dots.

*Source: notebook Section C, with four distribution figures covering eleven selected features.*

## 4. Relationships Between Features and Classification

The class comparisons use percentages within the phishing and legitimate groups. For example, the HTTPS percentage tells us how many phishing rows use HTTPS; it does not tell us the chance that an HTTPS URL is phishing.

### URL and Domain Length

Phishing URLs were generally longer and had more variation than legitimate URLs. The median recorded URL length was **34 characters for phishing and 26 for legitimate**. Phishing domains also tended to be slightly longer, although the two groups overlapped.

**So what?** URL length seems useful as one part of identifying phishing, but it cannot be used on its own. Some phishing URLs are short, and a longer URL does not automatically mean a site is phishing. This supports the teammate's URL-length finding and adds a comparison of domain lengths.

**What next?** Compare URL lengths among URLs with similar domain lengths. This could help show whether the difference comes mainly from the domain or from the rest of the URL, such as paths and queries. The recorded length differences should also be checked before choosing any cutoff.

The boxplots hide individual outlier markers to make the comparison easier to read. All rows are still included in the calculations, and the full ranges are shown elsewhere in the notebook.

*Source: notebook Section D, “Stored URL length by classification” and “Domain length by classification.”*

### Recorded Subdomain Counts

One subdomain was common in both groups, but it appeared more often in legitimate rows: about **85% compared with 63% of phishing rows**. Phishing rows were more likely to have three or more recorded subdomains. All rows with a recorded count of zero were phishing.

The average subdomain counts were almost the same for the two classes. Looking only at the averages would have hidden these differences.

**So what?** Subdomain count has a more complicated relationship with phishing than simply “more subdomains means more risk.” Both the zero-count group and the higher-count groups stood out. This could partly reflect how the dataset was collected or how subdomains were counted.

**What next?** Check how this feature was calculated and look at examples with a count of zero. It would also help to compare subdomain counts alongside HTTPS use and domain length.

*Source: notebook Section D, “Recorded subdomain counts by classification.”*

### URL and Webpage Indicators

HTTPS showed a large difference between the classes, but it was still present in nearly half of the phishing rows. Other features gave some unexpected results.

| Feature present | Phishing rows | Legitimate rows |
|---|---:|---:|
| HTTPS | About 49% | 100% |
| Obfuscation | Less than 1% | 0% |
| IP-based domain | Less than 1% | 0% |
| Recorded URL redirect | About 15% | About 12% |
| Password field | About 5% | About 14% |
| External form submission | Less than 1% | About 7% |

**So what?** HTTPS alone is not enough to judge whether a URL is legitimate. Obfuscation and IP-based domains only appeared in phishing rows in this dataset, but they were too rare to identify most phishing examples. Redirects showed a smaller difference between the classes, and the feature does not tell us how many redirects occurred.

Password fields and external form submission were actually more common in legitimate rows. This was surprising, but legitimate websites also use forms, so their presence is not automatically a warning sign. Webpage size may help explain this pattern: legitimate pages generally had far more lines of code than phishing pages. Differences in collection or feature extraction could also play a role.

**What next?** Compare form features among HTTPS pages and among pages of similar sizes. This would help check whether the same pattern holds when these other differences are taken into account.

*Source: notebook Section D, “URL and webpage indicators by classification.”*

## 5. Research Question and Next Steps

**Original research question:** Which features of phishing links and webpages make them harder for people to recognize?

This dataset can show differences between phishing and legitimate websites, but it does not include information about how people respond to them. A question we can answer more directly is:

**Which URL and webpage features differ between phishing and legitimate examples, especially when phishing examples also have HTTPS or ordinary-looking URL structures?**

The analysis shows that phishing and legitimate examples share several features. Many phishing rows use HTTPS, have one recorded subdomain, or have URL lengths that overlap with legitimate rows. These patterns could help us choose examples for a class activity, but they do not show which features actually fool people.

For the activity, we could compare how accurately people identify phishing examples with different HTTPS cues or URL structures, while keeping the other characteristics similar. Studying webpage appearance would also require screenshots or a controlled display, since features extracted from source code may not be visible to participants.

The next steps are to check how the features were extracted, examine combinations of features, and see whether the same patterns appear in our teammates' datasets. Repeated URLs, feature inconsistencies, and the way the data was collected limit how far we can apply these findings beyond PhiUSIIL. The cross-dataset analysis will be part of the group's combined work.
