# CS 418 Research Project

### Which URL and webpage features are shared by both phishing and legitimate websites, potentially making them harder to distinguish?


## Data documentation

See [DATASHEET.md](DATASHEET.md) for our codebooks, reproduction steps, and access and reuse details.

| Role | Dataset | Original source | License or terms |
|---|---|---|---|
| Primary | PhiUSIIL Phishing URL (UCI 967) | [UCI 967](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Primary | Phishing Websites (UCI 327) | [UCI 327](https://archive.ics.uci.edu/dataset/327/phishing) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Secondary | Website Phishing (UCI 379) | [UCI 379](https://archive.ics.uci.edu/dataset/379/website+phishing) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Secondary | Tranco Top Sites | [Tranco](https://tranco-list.eu/), [snapshot Y8YJG](https://tranco-list.eu/list/Y8YJG) | Redistribution license for this snapshot is unverified. The publisher lists upstream CC BY 3.0, CC BY-SA 4.0, and CC BY-NC 4.0 terms. Confirm the snapshot's terms before sharing the ranking. |

For the UCI datasets, reuse requires credit to the original creators, links to the source and license, and a description of any changes. PhishTank is an original collection source for the phishing datasets, not a separate dataset loaded by our notebooks.

Our data covers selected website samples and URL/webpage features, not how people respond to phishing. We can compare patterns in these samples, but we cannot say which features cause people to fall for phishing or assume the results apply to all websites.

## Dataset Notes:

### Primary Dataset #1:

**Source** UCI Machine Learning Repository
https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

This dataset contains URL and webpage characteristics for legitimate and phishing websites. We will use it as our main dataset to examine which URL, domain, security, and webpage features are associated with phishing.

- **Rows:** 235795
- **Columns:** 56
- **What one row represents:** Each row is a URL and it's corresponding webpage. Whether that's a legitimate URL or a phising URL.
- **Feature types:** Primarily numerical and binary features, with some categorical/text fields. Features cover URL structure, domain information, character patterns, security properties, and webpage characteristics.
- **Missing values:** None
- **Columns of interest:** `URLLength`, `DomainLength`, `IsDomainIP`, `NoOfSubDomain`, `HasObfuscation`, `ObfuscationRatio`, `DegitRatioInURL`, `SpacialCharRatioInURL`, `IsHTTPS`, `URLSimilarityIndex`, `TLDLegitimateProb`, `DomainTitleMatchScore`, `URLTitleMatchScore`, `HasFavicon`, `HasCopyrightInfo`, `HasSocialNet`, `HasPasswordField`, `HasSubmitButton`, and `label`
- **Class counts:** Label = 1 means legitimate URL and label = 0 means phishing URL
- **Data source/coverage:** Legitimate URLs were collected from the Open PageRank Initiative, while phishing URLs were collected from PhishTank, OpenPhish, and MalwareWorld.
- **Time coverage:** UCI only says that most URLs used to construct the dataset were recent/latest URLs at the time, and lists the dataset as created in 2024.
- **Geographic coverage:** Not specified. There is no location/country variable in UCI's listed features either. And no context is provided in the research paper either. 

### Primary Dataset #2: Phishing Websites

**Source:** UCI Machine Learning Repository  
https://archive.ics.uci.edu/dataset/327/phishing

This dataset contains website characteristics that can be used to distinguish phishing websites from legitimate websites. We will use it as a comparison dataset to examine which URL, domain, redirect, security, and webpage features are associated with phishing.

- **Rows:** 11,055
- **Columns:** 31 total (30 features and 1 target column, `Result`)
- **What one row represents:** One webpage represented by 30 extracted phishing-related features and its classification result
- **Feature types:** The source dataset encodes the features as integers, primarily using values such as -1, 0, and 1. When the ARFF file was initially loaded, the values were read as strings, so they were converted to integers in the notebook.
- **Missing values:** None.
- **Columns of interest:** `having_IP_Address`, `URL_Length`, `Shortining_Service`, `having_At_Symbol`, `Prefix_Suffix`, `having_Sub_Domain`, `SSLfinal_State`, `Redirect`, `age_of_domain`, `Google_Index`, and `Result`
- **Class counts:** `Result = -1` has 4,898 rows and `Result = 1` has 6,157 rows
- **Data source/coverage:** The dataset was collected mainly from the PhishTank archive, MillerSmiles archive, and Google search operators
- **Time coverage:** Exact collection dates are not documented by UCI. The dataset was donated on March 25, 2015; the introductory paper was published in 2012
- **Geographic coverage:** No specific geographic area is given; the dataset consists of websites collected from online sources rather than observations from a particular city or country

### Secondary Dataset #1: Website Phishing

**Source:** UCI Machine Learning Repository  
https://archive.ics.uci.edu/dataset/379/website+phishing

This dataset will be compared against our primary phishing datasets to examine whether URL, domain, traffic, and webpage-related features show similar patterns across different phishing datasets.

- **Rows:** 1,353
- **Columns:** 10 total (9 features and 1 target column, `Result`)
- **What one row represents:** One website represented by phishing-related features and its classification result
- **Feature types:** The source dataset encodes the features as integers using values such as -1, 0, and 1. When the ARFF file was initially loaded, the values were read as strings.
- **Missing values:** None
- **Columns of interest:** `URL_Length`, `having_IP_Address`, `SSLfinal_State`, `age_of_domain`, `web_traffic`, `Request_URL`, `URL_of_Anchor`, and `Result`
- **Class counts:** `Result = -1` has 702 phishing websites, `Result = 0` has 103 suspicious websites, and `Result = 1` has 548 legitimate websites
- **Data source/coverage:** The phishing websites were collected from the PhishTank archive, while legitimate websites were collected from Yahoo and Starting Point directories.
- **Time coverage:** A specific observation-level time span is not provided by UCI. The associated research paper was published in 2014, and the dataset was donated to UCI in 2016.
- **Geographic coverage:** No specific geographic area is given; the dataset consists of websites collected from online sources rather than observations from a particular city or country.

### Secondary Dataset #2: Tranco Top Sites

**Source:** Tranco

[https://tranco-list.eu/](https://tranco-list.eu/)

This dataset ranks popular website domains. We will use it as a comparison dataset to see how the structure of popular domains differs from phishing URLs.

- **Rows:** 1,000,000
- **Columns:** 2 original columns and 6 total after adding 4 domain structure features
- **What one row represents:** One domain and its popularity rank in the Tranco snapshot
- **Feature types:** `rank` and the two count features are integers, `domain` is a string, and the hyphen and number features are booleans
- **Missing values:** None. There are also no duplicate domains.
- **Columns of interest:** `rank`, `domain`, `domain_length`, `number_of_dots`, `contains_hyphen`, and `contains_number`
- **Data source/coverage:** The standard Tranco list contains pay-level domains rather than full URLs or subdomains
- **Time coverage:** The Y8YJG snapshot was generated on September 26, 2026, using rankings from August 28 to September 26, 2026. We downloaded it on September 27, 2026.
- **Geographic coverage:** The domains are not limited to a specific country. The dataset does not include a country column, so geographic representation cannot be measured directly.

We plan to compare these popular domains with domains from PhiUSIIL. Our current notebooks prepare the Tranco features but do not run this comparison yet. This will help us see whether features such as domain length, dot count, hyphens, and numbers differ between popular and phishing domains.

## Exploratory Analysis

For this checkpoint, we explored the datasets to get a better idea of what the features look like and how they relate to phishing classification. Most of our analysis focused on the PhiUSIIL dataset, the Website Phishing dataset, and the Phishing Website dataset.

### Revised Research Question

Our original question was:

**Which features of phishing links and webpages make them harder for people to recognize?**

After looking more closely at the data, we realized that the datasets do not actually measure whether a person was fooled by a phishing website. Because of that, we revised our question to:

**Which URL and webpage features are shared by both phishing and legitimate websites, potentially making them harder to distinguish?**

### Anomalies We Found

| Dataset | Anomaly | Rows affected | What we did |
|---|---|---:|---|
| PhiUSIIL | Repeated URLs | 850 rows across 425 URLs | Kept and flagged because the rows were not exact duplicates and had matching labels |
| PhiUSIIL | Stored URL length did not match the URL text | 187,151 | Kept and flagged because most differences were only one character |
| PhiUSIIL | HTTPS feature did not match the URL scheme | 493 | Kept and flagged for further review |
| PhiUSIIL | Very long URLs | 2,350 above the 99th percentile | Kept because long URLs can still be valid |
| Website Phishing | Duplicate feature/classification combinations | 629 | Kept because the dataset does not include unique website IDs, so we cannot confirm they are duplicate websites |
| Website Phishing | Columns originally loaded as strings | 1,353 | Converted the encoded feature values to integers |
| Both datasets | Missing values | 0 | No action needed |
| Phishing Websites (UCI 327) | Extra repeated feature/classification rows found in the final check | 5,206 | Kept because there are no website IDs to confirm duplicate websites |

### Main Findings

A few patterns stood out during the exploratory analysis:

- Phishing URLs in PhiUSIIL were generally longer than legitimate URLs. The median phishing URL length was 34 characters compared with 26 for legitimate URLs.
- Phishing URLs also tended to have a higher special-character ratio. This difference was still visible after splitting URLs into short, medium, and long groups.
- The IP address feature had a higher phishing rate in PhiUSIIL and the Website Phishing secondary dataset. However, IP-based domains were very rare in PhiUSIIL, so this feature would not identify most phishing websites by itself.
- HTTPS was common among legitimate websites, but almost half of the phishing rows in PhiUSIIL also used HTTPS. This shows that HTTPS alone is not enough to decide whether a website is legitimate.
- The two datasets showed some similar patterns, but they do not always measure features in exactly the same way, so the results should be compared carefully.
- In the Phishing Websites primary dataset, 736 phishing websites had URL lengths categorized as legitimate. This shows that phishing websites don't necessarily have suspicious-looking URL lengths.
- When looking at subdomains, 810 phishing websites had subdomain characteristics categorized as legitimate. This suggests that some phishing websites have normal-looking domain structures.
- SSL characteristics also stood out, with 701 phishing websites having SSL characteristics categorized as legitimate. This shows that phishing websites can still have security-related characteristics typically associated with legitimate websites.
- When comparing SSL characteristics between the Phishing Websites primary and Website Phishing secondary datasets, the legitimate-associated category (1) was the most common in both, accounting for 57.27% and 55.51% of websites, respectively. However, these percentages include both phishing and legitimate websites.

Overall, the EDA suggests that combinations of URL and webpage features may be more useful than relying on one feature by itself. Our next steps are to continue comparing features across datasets and focus on patterns that appear consistently.



Group members: Srijani Prekki, Catherine Carter, Zainab Ahmed, Mehtab Kaur
