# Data Documentation

## Dataset Inventory

### Primary Datasets

1. **PhiUSIIL Phishing URL (Website)** — UCI #967
2. **Phishing Websites** — UCI #327

### Secondary Datasets

1. **Website Phishing** — UCI #379
2. **Tranco Top Sites**

---

# 1. Primary Dataset Datasheets

## Primary Dataset #1: PhiUSIIL Phishing URL (Website)

Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset)  

Version reference: [Mendeley Version 2](https://data.mendeley.com/datasets/shwpxscxy2/2). Our local file matches the current UCI download; its identity with Mendeley v2 has not been checked.

Dataset DOI: 10.17632/shwpxscxy2.2

### 1. Motivation  

The PhiUSIIL dataset was created to help researchers study and detect phishing websites, which are fake or misleading websites that try to look trustworthy so that users will click on them or give away information such as passwords or financial info. They wanted to build a large dataset that included both phishing and legit websites and many different characteristics of their URLs and webpages. These features could then be used to train and test machine learning models for phishing detection. The dataset was created by Arvind Prasad and Shalini Chandra. According to the [research paper](https://doi.org/10.1016/j.cose.2023.103545), the authors didn't receive funding or support from an organization for this work.

### 2. Composition

The dataset has 235,795 rows, which represents a URL and its corresponding webpage. UCI lists 54 predictive features in the dataset. The CSV file used by our group contains 56 columns total because it also contains the FILENAME identifier column and the label target column.

- The dataset contains two classes
- Phishing: 100,945 rows
- Legitimate: 134,850 rows
- Label = 0: phishing
- Label = 1: legitimate
- Missing values: None reported by UCI

The features describe different parts of a URL or webpage, such as URL length, domain length, whether the domain uses an IP address, number of subdomains, HTTPS use, special characters, webpage size, redirects, forms, password fields, and other webpage characteristics.

This dataset is a sample of phishing and legitimate websites collected from specific online sources, so results from this dataset should not automatically be assumed to represent the entire web.

During our exploratory analysis, our group also found some things that should be kept in mind when using the data. For example, 850 rows represented 425 URLs that appeared more than once. We also found that the stored URLLength did not exactly match the displayed URL text for many rows, and 493 rows had an IsHTTPS value that did not match the URL scheme. We kept these rows because we couldn't confirm that they were actual errors.


### 3. Collection Process

The researchers collected phishing and legitimate URLs, downloaded the webpages, and extracted features from the URLs and HTML, as described in the [paper](https://doi.org/10.1016/j.cose.2023.103545). UCI says most URLs were recent when the dataset was constructed. The public dataset records do not give the full sampling rules or say whether website owners were notified or gave consent.

### 4. Preprocessing 

Before the dataset was released, the researchers extracted features from both the URL itself and the source code of its webpage. Some features are direct measurements, such as URL length or number of subdomains. Other features were calculated or derived from existing information. For example CharContinuationRate, URLTitleMatchScore, URLCharProb, and TLDLegitimateProb.

The dataset was also already labeled before we starting doing stuff, with 0 representing phishing and 1 representing legitimate.

The publicly released dataset is provided as a CSV containing the URLs and extracted features. The UCI and Mendeley releases list the processed CSV as the publicly available dataset file. Separate raw HTML webpage files are not listed in those public releases. Also, our group didn't remove rows during our initial exploratory analysis. We kept unusual or repeated observations and documented them instead of assuming they were errors.

### 5. Uses  


The dataset was created mainly for research on phishing website detection and classification. The original researchers used it to test the PhiUSIIL phishing detection framework and machine learning methods.

Our group is using the dataset to study which URL and webpage characteristics are associated with phishing classification. We're' also comparing some of these patterns with other phishing datasets to see whether similar warning signs appear across datasets.

There are some things about this dataset that we should all make a note of. It doesn't measure whether a real person would recognize or fall for a phishing website, so we can't use it by itself to say which characteristics make a phishing website more convincing to humans. Also, as mentioned earlier, these are based of a sample of websites, so they don't speak for all websites out there. 


### 6. Distribution  

The PhiUSIIL dataset is publicly available through the UCI Machine Learning Repository and Mendeley Data.

- File format: CSV   
- Main file: PhiUSIIL_Phishing_URL_Dataset.csv  
- File size: approximately 54.2 MB  
- Mendeley version: Version 2  
- Version 2 publication date: November 15, 2023  
- Dataset DOI: 10.17632/shwpxscxy2.2  
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)  
- Project access dates: October 26, 2026 (previously recorded); October 28, 2026 (download rechecked)
- The CC BY 4.0 license allows other people to share and adapt the dataset as long as they give proper credit to the original creators.

### 7. Maintenance  

The dataset is currently hosted by both the UCI Machine Learning Repository and Mendeley Data. The Mendeley record shows that there have been at least two published versions. Version 1 was published on August 29, 2023, and Version 2 was published on November 15, 2023. Version 2 is the latest version currently listed on Mendeley. UCI lists the dataset as donated on March 3, 2024. A regular schedule for future updates is not documented by the publisher. Someone reusing the dataset in the future could try checking the UCI page and the Mendeley version history to see whether a newer version has been released.

---

## Primary Dataset #2: Phishing Websites

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/327/phishing)

**Dataset DOI:** https://doi.org/10.24432/C51W2X

### 1. Motivation

The Phishing Websites dataset was created to help researchers identify which website characteristics are useful for identifying phishing websites from legit websites. The researchers explained that reliable training datasets for phishing detection were difficult to find, so they wanted to provide a dataset containing important phishing-related features and introduce additional features that could improve phishing detection.

UCI credits Rami Mohammad and Lee McCluskey. The linked Huddersfield record also credits Fadi Thabtah.

**Funding:** Not documented by the publisher.

**Sources:**
- [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)
- [University of Huddersfield Dataset Record](https://eprints.hud.ac.uk/id/eprint/24330/)

### 2. Composition

The Phishing Websites dataset contains **11,055 rows and 31 columns** (30 features and 1 classification column).

Each row represents one website with features related to its URL, domain, security, and webpage characteristics. The `Result` column identifies whether a website is phishing (-1) or legitimate (1).

- **Phishing websites:** 4,898
- **Legitimate websites:** 6,157
- **Repeated feature/classification rows:** 5,206 extra occurrences, found in the final data check and kept because there are no website IDs
- **Missing values:** None
- **Data sources:** PhishTank, MillerSmiles, and Google search operators.

The dataset is a sample of websites from these sources, not every website on the internet.

**Limitations:** The dataset does not specify geographic coverage or exact collection dates. It also lacks unique website IDs, making it difficult to identify duplicate websites. Because the data comes from selected sources, it may not represent all websites.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

### 3. Collection Process

The dataset was collected mainly from PhishTank, MillerSmiles, and Google search operators. Researchers gathered phishing and legitimate websites and extracted features related to their URLs, domains, and webpage characteristics.

- **Collection method:** Online website records and automated feature extraction.
- **Time frame:** The dataset was submitted to UCI on March 25, 2015, but the exact collection dates are not documented by the publisher.
- **Consent:** The dataset describes websites rather than individual participants. Whether website owners were notified or gave consent is not documented by the publisher.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

### 4. Preprocessing

The researchers extracted phishing-related features from websites and converted them into numerical values such as -1, 0, and 1.

- **Cleaning:** Any additional cleaning or removal of records before publication is not documented by the publisher.
- **Missing values:** The published dataset has no missing values.
- **Raw data:** The extracted features are available in the `Training Dataset.arff` file, but the original website data used to create them is not provided.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

### 5. Uses

The dataset has been used in research to identify phishing websites and develop machine learning models for phishing detection.

Our group is using it to compare URL and webpage features associated with phishing across different datasets.

**Limitations:** The dataset should not be used to determine whether a person would recognize a phishing website. It also should not be used as the only method for detecting phishing because website characteristics and phishing techniques can change over time.

**Sources:**
- [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)
- [Predicting Phishing Websites Based on Self-Structuring Neural Network](https://eprints.hud.ac.uk/id/eprint/19220/)

### 6. Distribution

The dataset is available to the public through the UCI Machine Learning Repository. It can be downloaded as an ARFF file or accessed using Python's `ucimlrepo` package.

- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Reuse:** Others can copy, share, and modify the dataset as long as they give proper credit to the original creators.
- **Access:** Free and publicly available.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

### 7. Maintenance

The dataset is hosted by the UCI Machine Learning Repository and was donated on March 25, 2015.

- **Maintenance:** UCI hosts the dataset, but who is responsible for maintaining its contents is not documented by the publisher.
- **Updates:** No regular update schedule is documented.
- **New versions:** Users can check the UCI dataset page for any changes or updates.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

---

# 2. Scope

**Current group research question:** Which URL and webpage features are shared by both phishing and legitimate websites, potentially making them harder to distinguish?

We study shared technical features and classification patterns. The phrase "harder to distinguish" is our motivation, not a measured human-recognition result. The PhiUSIIL-only follow-up question uses Dataset 1's scope below; comparisons across datasets use the relevant samples listed here.

### Dataset 1: PhiUSIIL Phishing URL Dataset (UCI 967)

- **Target Population:** All phishing and legitimate websites that people may encounter online, particularly those that share similar URL and webpage features.
- **Access Frame:** The phishing and legitimate websites available through the sources used by the researchers who constructed the PhiUSIIL dataset. The exact boundaries of this access frame are not fully established by the dataset alone.
- **Sample:** 235,795 website records, including 100,945 phishing websites and 134,850 legitimate websites. The dataset contains 56 columns, including URL length, HTTPS usage, domain characteristics, redirects, and webpage features.

### Dataset 2: Phishing Websites Dataset (UCI 327)

- **Target Population:** All phishing and legitimate websites that people may encounter online, particularly those that share URL and webpage characteristics that could make them difficult to distinguish.
- **Access Frame:** Websites collected through PhishTank, MillerSmiles, and Google search operators, as listed by UCI. The complete set of websites eligible for collection is not fully documented.
- **Sample:** 11,055 website records, including 4,898 phishing websites and 6,157 legitimate websites. The dataset contains 30 features and one classification column, including URL length, subdomains, SSL certificate status, redirects, and other webpage characteristics.

### Secondary Dataset 1: Website Phishing (UCI 379)

- **Target Population:** Phishing, suspicious, and legitimate websites with the URL and webpage characteristics we compare.
- **Access Frame:** Websites collected by the original researchers from PhishTank, Yahoo, and Starting Point directories, as described by [UCI](https://archive.ics.uci.edu/dataset/379/website+phishing). Full sampling rules are not documented there.
- **Sample:** 1,353 records with 9 features and `Result`: 702 phishing, 103 suspicious, and 548 legitimate. Only the IP comparison excludes the 103 suspicious rows, leaving 1,250 records.

### Secondary Dataset 2: Tranco Top Sites

- **Target Population:** Popular pay-level domains, not all websites or a verified set of legitimate websites.
- **Access Frame:** Domains represented in the CrUX, Farsight, Majestic, Cloudflare Radar, and Cisco Umbrella rankings used by [snapshot Y8YJG](https://tranco-list.eu/api/lists/id/Y8YJG), covering August 28 to September 26, 2026.
- **Sample:** 1,000,000 ranked domains, with two original columns and four domain features added by our notebook. The cross-dataset domain comparison is still planned.

### Limitations of Our Data

Our datasets only represent a portion of the phishing and legitimate websites that exist online, so our findings may not apply to every website. Since the datasets were collected from specific sources rather than randomly sampling all websites, they may not accurately represent the types of websites people commonly encounter.

Another limitation is the year the data was collected. Phishing techniques change and advance over time, and older datasets may not reflect newer methods used to make phishing websites appear legitimate.

The two datasets also contain different features and use different methods to measure them. For example, the PhiUSIIL dataset records URL length as a numerical value, while the Phishing Websites dataset categorizes URL length into predefined values. This makes direct comparisons between the datasets more challenging.

Also, some features, such as domain registration information and webpage source code characteristics, are not directly visible to everyday users. This limits our ability to determine which shared features might make a phishing website appear legitimate to someone just casually browsing the internet.

Finally, although we can identify URL and webpage features shared by phishing and legitimate websites, our datasets do not measure how well people can recognize phishing attempts. So we can't directly conclude whether these shared features actually make websites harder for people to distinguish.

---

# 3. Codebooks

## PhiUSIIL

## PhiUSIIL Codebook

The first table covers columns used in our main comparisons and the row-level columns we created. The next table adds the other source columns checked during profiling and validation.

| Column | Data Type | Units | Meaning | Range / Allowed Values | Missing Values | Origin |
|---|---|---|---|---|---|---|
| `FILENAME` | string | N/A | Identifier for the webpage record in the dataset | Text filename such as `521848.txt` | None | Original PhiUSIIL dataset |
| `URL` | string | N/A | Full URL of the website | URL text | None | Original PhiUSIIL dataset |
| `URLLength` | integer | characters | Length of the URL recorded by the publisher | Observed from 13 to 6,097 characters | None | Original PhiUSIIL dataset |
| `Domain` | string | N/A | Domain portion of the website URL | Domain text | None | Original PhiUSIIL dataset |
| `DomainLength` | integer | characters | Length of the domain | Positive integer; observed maximum of 110 | None | Original PhiUSIIL dataset |
| `IsDomainIP` | integer | indicator | Whether the domain is written as an IP address instead of a regular domain name | `0` = no, `1` = yes | None | Original PhiUSIIL dataset |
| `TLD` | string | N/A | Top-level domain of the website, such as `com`, `org`, or `uk` | Text | None | Original PhiUSIIL dataset |
| `TLDLength` | integer | characters | Length of the top-level domain | Positive integer | None | Original PhiUSIIL dataset |
| `NoOfSubDomain` | integer | count | Publisher-recorded number of subdomains in the URL | Observed values from 0 to 10 | None | Original PhiUSIIL dataset |
| `HasObfuscation` | integer | indicator | Whether URL obfuscation was detected | `0` = no, `1` = yes | None | Original PhiUSIIL dataset |
| `NoOfObfuscatedChar` | integer | count | Number of characters in the URL identified as obfuscated | Nonnegative integer | None | Original PhiUSIIL dataset |
| `SpacialCharRatioInURL` | float | proportion | Proportion of the URL made up of special characters | Observed from 0 to about 0.397 | None | Original PhiUSIIL dataset |
| `IsHTTPS` | integer | indicator | Whether the publisher recorded the URL as using HTTPS | `0` = no, `1` = yes | None | Original PhiUSIIL dataset |
| `LineOfCode` | integer | lines | Number of lines of source code recorded for the webpage | Positive integer; observed maximum of 442,666 | None | Original PhiUSIIL dataset |
| `LargestLineLength` | integer | characters | Length of the longest line in the webpage source code | Nonnegative integer | None | Original PhiUSIIL dataset |
| `HasTitle` | integer | indicator | Whether the webpage was recorded as having a title | `0` = no, `1` = yes | None | Original PhiUSIIL dataset |
| `Title` | string | N/A | Recorded webpage title | Text; some rows use values such as `0` or `na` | None reported by publisher | Original PhiUSIIL dataset |
| `NoOfURLRedirect` | integer | indicator/count | Records whether a URL redirect was present in this dataset | Observed values are `0` and `1` | None | Original PhiUSIIL dataset |
| `HasExternalFormSubmit` | integer | indicator | Whether the webpage contains a form that submits to an external location | `0` = no, `1` = yes | None | Original PhiUSIIL dataset |
| `HasPasswordField` | integer | indicator | Whether the webpage contains a password input field | `0` = no, `1` = yes | None | Original PhiUSIIL dataset |
| `label` | integer | category | Classification of the website | `0` = phishing, `1` = legitimate | None | Publisher-provided classification label |
| `URLTextLength` | integer | characters | Length of the URL calculated directly from the `URL` text so we could compare it with `URLLength` | Positive integer | None | Derived in `notebooks/eda_phiusiil.ipynb` from `URL` |
| `HTTPSFromURL` | integer | indicator | Whether the URL text itself begins with `https://`, used to compare against `IsHTTPS` | `0` = no, `1` = yes | None | Derived in `notebooks/eda_phiusiil.ipynb` from `URL` |
| `subdomain_group` | string/category | N/A | Groups the number of subdomains into broader categories for comparison | `0`, `1`, `2`, `3+` | None | Derived in `notebooks/eda_phiusiil.ipynb` from `NoOfSubDomain` |
| `length_group` | category | N/A | Groups URLs by length for comparing special-character ratios among similar-length URLs | `Short (25 or less)`, `Medium (26-40)`, `Long (41+)` | None | Derived in `notebooks/eda_checkpoint_three.ipynb` from `URLLength` |


### Other PhiUSIIL columns checked in the notebook

These columns are included in the profile or validation checks in [eda_phiusiil.ipynb](notebooks/eda_phiusiil.ipynb), Sections A and B. Types and ranges below come from the local CSV. Names match the [UCI variable list](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset). We keep the publisher's features rather than recalculating them. The public dataset pages do not fully explain the score formulas or every webpage-flag extraction rule, so those details still need the full paper or author code. Zero is a recorded value here, not a missing-value marker.

| Column | Data Type | Units | Meaning | Range / Allowed Values | Missing Values | Origin |
|---|---|---|---|---|---|---|
| `URLSimilarityIndex` | float (`Float64`) | score | Publisher-provided URL similarity score | Observed 0.155574352 to 100.0 | None observed | Original PhiUSIIL dataset |
| `CharContinuationRate` | float (`Float64`) | proportion | Publisher-provided character-continuation rate | Observed 0.0 to 1.0 | None observed | Original PhiUSIIL dataset |
| `TLDLegitimateProb` | float (`Float64`) | probability | Publisher-provided legitimate probability for the TLD | Observed 0.0 to 0.5229071 | None observed | Original PhiUSIIL dataset |
| `URLCharProb` | float (`Float64`) | probability | Publisher-provided URL character probability | Observed 0.001082764 to 0.090823664 | None observed | Original PhiUSIIL dataset |
| `ObfuscationRatio` | float (`Float64`) | proportion | Publisher-recorded ratio of obfuscated URL characters | Observed 0.0 to 0.348 | None observed | Original PhiUSIIL dataset |
| `NoOfLettersInURL` | integer (`Int64`) | characters | Recorded number of letters in the URL | Observed 0 to 5191 | None observed | Original PhiUSIIL dataset |
| `LetterRatioInURL` | float (`Float64`) | proportion | Recorded ratio of letters in the URL | Observed 0.0 to 0.926 | None observed | Original PhiUSIIL dataset |
| `NoOfDegitsInURL` | integer (`Int64`) | characters | Recorded number of digits in the URL; original spelling kept | Observed 0 to 2011 | None observed | Original PhiUSIIL dataset |
| `DegitRatioInURL` | float (`Float64`) | proportion | Recorded ratio of digits in the URL; original spelling kept | Observed 0.0 to 0.684 | None observed | Original PhiUSIIL dataset |
| `NoOfEqualsInURL` | integer (`Int64`) | count | Recorded number of equals signs in the URL | Observed 0 to 176 | None observed | Original PhiUSIIL dataset |
| `NoOfQMarkInURL` | integer (`Int64`) | count | Recorded number of question marks in the URL | Observed 0 to 4 | None observed | Original PhiUSIIL dataset |
| `NoOfAmpersandInURL` | integer (`Int64`) | count | Recorded number of ampersands in the URL | Observed 0 to 149 | None observed | Original PhiUSIIL dataset |
| `NoOfOtherSpecialCharsInURL` | integer (`Int64`) | count | Recorded number of other special characters in the URL | Observed 0 to 499 | None observed | Original PhiUSIIL dataset |
| `DomainTitleMatchScore` | float (`Float64`) | score | Publisher-provided domain/title matching score | Observed 0.0 to 100.0 | None observed | Original PhiUSIIL dataset |
| `URLTitleMatchScore` | float (`Float64`) | score | Publisher-provided URL/title matching score | Observed 0.0 to 100.0 | None observed | Original PhiUSIIL dataset |
| `HasFavicon` | integer (`Int64`) | indicator | Publisher flag for a webpage favicon | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `Robots` | integer (`Int64`) | indicator | Publisher-provided robots-related webpage flag | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `IsResponsive` | integer (`Int64`) | indicator | Publisher-provided webpage responsiveness flag | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `NoOfSelfRedirect` | integer (`Int64`) | count/indicator | Publisher-recorded self-redirect feature; only 0 and 1 occur | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `HasDescription` | integer (`Int64`) | indicator | Publisher flag for a webpage description | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `NoOfPopup` | integer (`Int64`) | count | Publisher-recorded number of pop-up windows | Observed 0 to 602 | None observed | Original PhiUSIIL dataset |
| `NoOfiFrame` | integer (`Int64`) | count | Publisher-recorded number of iframes | Observed 0 to 1602 | None observed | Original PhiUSIIL dataset |
| `HasSocialNet` | integer (`Int64`) | indicator | Publisher flag for social-network content or links | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `HasSubmitButton` | integer (`Int64`) | indicator | Publisher flag for a submit button | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `HasHiddenFields` | integer (`Int64`) | indicator | Publisher flag for hidden form fields | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `Bank` | integer (`Int64`) | indicator | Publisher-provided bank-related webpage flag | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `Pay` | integer (`Int64`) | indicator | Publisher-provided payment-related webpage flag | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `Crypto` | integer (`Int64`) | indicator | Publisher-provided cryptocurrency-related webpage flag | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `HasCopyrightInfo` | integer (`Int64`) | indicator | Publisher flag for copyright information | `0`, `1` | None observed | Original PhiUSIIL dataset |
| `NoOfImage` | integer (`Int64`) | count | Publisher-recorded number of images | Observed 0 to 8956 | None observed | Original PhiUSIIL dataset |
| `NoOfCSS` | integer (`Int64`) | count | Publisher-recorded number of CSS resources | Observed 0 to 35820 | None observed | Original PhiUSIIL dataset |
| `NoOfJS` | integer (`Int64`) | count | Publisher-recorded number of JavaScript resources | Observed 0 to 6957 | None observed | Original PhiUSIIL dataset |
| `NoOfSelfRef` | integer (`Int64`) | count | Publisher-recorded self-reference count | Observed 0 to 27397 | None observed | Original PhiUSIIL dataset |
| `NoOfEmptyRef` | integer (`Int64`) | count | Publisher-recorded empty-reference count | Observed 0 to 4887 | None observed | Original PhiUSIIL dataset |
| `NoOfExternalRef` | integer (`Int64`) | count | Publisher-recorded external-reference count | Observed 0 to 27516 | None observed | Original PhiUSIIL dataset |

## Phishing Websites

We use all 30 features in the category-count tables, along with `Result`. The names below match [Training Dataset.arff](datasets/phishing-websites/Training%20Dataset.arff). They load as strings and are converted to `Int64` in [phishing_websites_exploration.ipynb](notebooks/phishing_websites_exploration.ipynb) and [eda_primary_phishing_websites.ipynb](notebooks/eda_primary_phishing_websites.ipynb).

The feature meanings come from the publisher's [Phishing Websites Features guide](datasets/phishing-websites/Phishing%20Websites%20Features.docx), listed on the [UCI page](https://archive.ics.uci.edu/dataset/327/phishing). These are category codes, not raw measurements or the website's final class. We checked every allowed set against the ARFF header and the observed data. There are no missing values. In [ARFF](https://ml.cms.waikato.ac.nz/weka/arff.html), `?` marks a missing value; `-1` and `0` here are actual category values.

| Column | Data Type | Units | Meaning | Range / Allowed Values | Missing Values | Origin |
|---|---|---|---|---|---|---|
| `having_IP_Address` | integer (`Int64`) | category | IP address used in place of a domain name | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `URL_Length` | integer (`Int64`) | category | URL length category, not a character count | `-1`, `0`, `1` | None; `?` absent | Original UCI 327 |
| `Shortining_Service` | integer (`Int64`) | category | Use of a URL shortening service | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `having_At_Symbol` | integer (`Int64`) | category | Presence of an @ symbol in the URL | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `double_slash_redirecting` | integer (`Int64`) | category | Position of a double slash in the URL beyond the protocol | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Prefix_Suffix` | integer (`Int64`) | category | Hyphen-separated prefix or suffix in the domain name | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `having_Sub_Domain` | integer (`Int64`) | category | Category based on the number of subdomains | `-1`, `0`, `1` | None; `?` absent | Original UCI 327 |
| `SSLfinal_State` | integer (`Int64`) | category | HTTPS and certificate characteristics, not just HTTPS presence | `-1`, `0`, `1` | None; `?` absent | Original UCI 327 |
| `Domain_registeration_length` | integer (`Int64`) | category | Category based on how long the domain is registered for | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Favicon` | integer (`Int64`) | category | Whether the favicon comes from the same domain as the webpage | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `port` | integer (`Int64`) | category | Whether network ports have the open/closed status expected by the publisher | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `HTTPS_token` | integer (`Int64`) | category | Use of the HTTPS token in the domain name | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Request_URL` | integer (`Int64`) | category | Category based on embedded objects loaded from other domains | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `URL_of_Anchor` | integer (`Int64`) | category | Category based on anchor links pointing elsewhere or not linking to a webpage | `-1`, `0`, `1` | None; `?` absent | Original UCI 327 |
| `Links_in_tags` | integer (`Int64`) | category | Category based on external links in meta, script, and link tags | `-1`, `0`, `1` | None; `?` absent | Original UCI 327 |
| `SFH` | integer (`Int64`) | category | Server form handler category, based on where submitted form data goes | `-1`, `0`, `1` | None; `?` absent | Original UCI 327 |
| `Submitting_to_email` | integer (`Int64`) | category | Use of mail functions to send submitted information to email | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Abnormal_URL` | integer (`Int64`) | category | Whether the URL matches the website identity in WHOIS records | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Redirect` | integer (`Int64`) | category | Website forwarding category, not a redirect count | `0`, `1` | None; `?` absent | Original UCI 327 |
| `on_mouseover` | integer (`Int64`) | category | Whether a mouse-over event changes the browser status bar | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `RightClick` | integer (`Int64`) | category | Whether right-click is disabled | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `popUpWidnow` | integer (`Int64`) | category | Use of a pop-up window asking for personal information | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Iframe` | integer (`Int64`) | category | Use of iframe redirection or hidden frames | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `age_of_domain` | integer (`Int64`) | category | Domain age category, not an age in days or months | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `DNSRecord` | integer (`Int64`) | category | Whether a DNS record was found | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `web_traffic` | integer (`Int64`) | category | Website traffic/ranking category, not a visitor count | `-1`, `0`, `1` | None; `?` absent | Original UCI 327 |
| `Page_Rank` | integer (`Int64`) | category | PageRank category, not the original PageRank score | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Google_Index` | integer (`Int64`) | category | Whether the website appears in the Google index | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Links_pointing_to_page` | integer (`Int64`) | category | Category based on links pointing to the webpage | `-1`, `0`, `1` | None; `?` absent | Original UCI 327 |
| `Statistical_report` | integer (`Int64`) | category | Whether the domain or IP appears in the phishing reports used by the publisher | `-1`, `1` | None; `?` absent | Original UCI 327 |
| `Result` | integer (`Int64`) | category | Website classification | `-1` = phishing; `1` = legitimate | None; `?` absent | Original UCI 327 |

### Names changed in the EDA

The primary EDA and combined [eda.ipynb](notebooks/eda.ipynb) rename two columns after loading. These are spelling changes only; the values and types stay the same. The exploration notebook keeps the original names.

| Column | Data Type | Units | Meaning | Range / Allowed Values | Missing Values | Origin |
|---|---|---|---|---|---|---|
| `Shortening_Service` | integer (`Int64`) | category | Same feature as `Shortining_Service` | `-1`, `1` | None | Renamed in [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `Domain_registration_length` | integer (`Int64`) | category | Same feature as `Domain_registeration_length` | `-1`, `1` | None | Renamed in [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |

## Secondary Dataset Variables Used

### Website Phishing (UCI 379)

All nine features are plotted in [eda_secondary.ipynb](notebooks/eda_secondary.ipynb), and `Result` is used for class counts and comparisons. [website_phishing_secondary.ipynb](notebooks/website_phishing_secondary.ipynb) first loads them as strings. The table shows the integer types used after decoding and conversion in the EDA and [eda_checkpoint_three.ipynb](notebooks/eda_checkpoint_three.ipynb). The SSL-only comparison in the primary EDA converts only `SSLfinal_State`; its other secondary columns stay strings.

We checked the names and allowed values against [PhishingData.arff](datasets/website-phishing/PhishingData.arff) and the [UCI record](https://archive.ics.uci.edu/dataset/379/website+phishing). The file spells `popUpWidnow` differently from the page's `popUpWindow`, so we keep the file's name. UCI describes `-1`, `0`, and `1` as phishing, suspicious, and legitimate categories, but does not give full feature thresholds or explain the IP feature's `0`/`1` mapping. We do not assume that features with the same names have the same rules as UCI 327. No `?` values or nulls were found; `0` and `-1` are not missing values.

| Column | Data Type | Units | Meaning | Range / Allowed Values | Missing Values | Origin |
|---|---|---|---|---|---|---|
| `SFH` | integer (`int64`) | category | Server form handler category, describing where form data is submitted | `-1`, `0`, `1` | None; `?` absent | Original UCI 379 |
| `popUpWidnow` | integer (`int64`) | category | Pop-up window feature category | `-1`, `0`, `1` | None; `?` absent | Original UCI 379 |
| `SSLfinal_State` | integer (`int64`) | category | SSL-related feature category, not a direct HTTPS indicator | `-1`, `0`, `1` | None; `?` absent | Original UCI 379 |
| `Request_URL` | integer (`int64`) | category | Category related to objects requested from other domains | `-1`, `0`, `1` | None; `?` absent | Original UCI 379 |
| `URL_of_Anchor` | integer (`int64`) | category | Anchor-link feature category | `-1`, `0`, `1` | None; `?` absent | Original UCI 379 |
| `web_traffic` | integer (`int64`) | category | Website traffic category, not a visitor count | `-1`, `0`, `1` | None; `?` absent | Original UCI 379 |
| `URL_Length` | integer (`int64`) | category | URL length category, not a character count | `-1`, `0`, `1` | None; `?` absent | Original UCI 379 |
| `age_of_domain` | integer (`int64`) | category | Domain age category, not an age in days or months | `-1`, `1` | None; `?` absent | Original UCI 379 |
| `having_IP_Address` | integer (`int64`) | category | IP-address feature; the UCI page does not explain this file’s exact 0/1 mapping | `0`, `1` | None; `?` absent | Original UCI 379 |
| `Result` | integer (`int64`) | category | Website classification | `-1` = phishing; `0` = suspicious; `1` = legitimate | None; `?` absent | Original UCI 379 |

The temporary `secondary_binary` dataframe keeps only `Result = -1` or `1`. It has the same columns and adds no new variables.

### Tranco Top Sites

[tranco_data_acquisition.ipynb](notebooks/tranco_data_acquisition.ipynb) loads `rank` and `domain` from the headerless Y8YJG CSV and adds the four domain features below. The ranges are from our local snapshot. There are no nulls or blank domains. The [Tranco publisher](https://tranco-list.eu/) describes this as a popularity ranking; it does not supply phishing/legitimate labels. Dot count is not a subdomain count.

| Column | Data Type | Units | Meaning | Range / Allowed Values | Missing Values | Origin |
|---|---|---|---|---|---|---|
| `rank` | integer (`Int64`) | rank | Domain popularity rank; a smaller number ranks higher | 1 to 1,000,000 | None | Original Tranco CSV; named by our notebook |
| `domain` | string | N/A | Ranked domain name, not a full URL | Domain text; observed length 4 to 68 characters | None; no blank domains | Original Tranco CSV; named by our notebook |
| `domain_length` | integer (`UInt32`) | characters | Character length of `domain` | Observed 4 to 68 | None | Derived in [Tranco notebook](notebooks/tranco_data_acquisition.ipynb) using `str.len_chars()` |
| `number_of_dots` | integer (`UInt32`) | count | Number of literal dots in `domain` | Observed 1 to 3 | None | Derived in [Tranco notebook](notebooks/tranco_data_acquisition.ipynb) using `str.count_matches(r"\.")` |
| `contains_hyphen` | boolean | indicator | Whether `domain` contains a hyphen | `false` = no; `true` = yes | None | Derived in [Tranco notebook](notebooks/tranco_data_acquisition.ipynb) using a literal `-` check |
| `contains_number` | boolean | indicator | Whether `domain` contains an ASCII digit | `false` = no; `true` = yes | None | Derived in [Tranco notebook](notebooks/tranco_data_acquisition.ipynb) using `[0-9]` |

## Other Derived Variables and Analysis Summaries

The PhiUSIIL table above already covers `URLTextLength`, `HTTPSFromURL`, `subdomain_group`, and `length_group`. The table below adds the remaining derived columns, including columns in temporary summaries used for checks and plots. These do not add new website records. The matching parts of [eda.ipynb](notebooks/eda.ipynb) repeat these calculations.

| Column | Data Type | Units | Meaning | Range / Allowed Values | Missing Values | Origin |
|---|---|---|---|---|---|---|
| `length_offset` | integer (`Int64`) | characters | Stored `URLLength` minus `URLTextLength` | Observed -35 to 0 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `classification` | string | N/A | Class name made from PhiUSIIL `label` in the length-group summary | `Phishing`, `Legitimate` | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `ip_feature` | integer (`int64`) | category | Renamed IP feature in each dataset’s summary; original coding is kept | `0`, `1` | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `phishing_rate` | float (`float64`) | percent | 100 × phishing rows / rows in each IP group; uses `label = 0` for PhiUSIIL and `Result = -1` in the secondary binary subset | 0 to 100 | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `dataset` | string | N/A | Identifies which dataset an IP summary comes from | `PhiUSIIL`, `Website Phishing` | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `PhiUSIIL` | float (`float64`) | percent | Dataset-specific `phishing_rate` column after pivoting `ip_compare` | 0 to 100 | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb), `ip_plot` |
| `Website Phishing` | float (`float64`) | percent | Dataset-specific `phishing_rate` column after pivoting `ip_compare` | 0 to 100 | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb), `ip_plot` |
| `Phishing` | integer (`int64`) or float (`float64`) | count, proportion, or percent | Class count in `length_counts`; median special-character ratio in `median_plot`; within-feature class percentage in secondary crosstabs | Counts ≥ 0; ratios 0 to 1; percentages 0 to 100 | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) and [secondary EDA](notebooks/eda_secondary.ipynb) |
| `Legitimate` | integer (`int64`) or float (`float64`) | count, proportion, or percent | Class count in `length_counts`; median special-character ratio in `median_plot`; within-feature class percentage in secondary crosstabs | Counts ≥ 0; ratios 0 to 1; percentages 0 to 100 | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) and [secondary EDA](notebooks/eda_secondary.ipynb) |
| `Suspicious` | float (`float64`) | percent | Within-feature percentage with `Result = 0` in secondary crosstabs | 0 to 100 | None observed | [secondary EDA](notebooks/eda_secondary.ipynb) |
| `Feature` | string | N/A | Feature name in the three code-frequency tables | The 30 UCI 327 feature names, with the two EDA spelling changes | None observed | [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `-1 Count` | integer (`Int64`) | count | Number of websites whose feature has code -1 | 0 to 11,055 | None observed | [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `0 Count` | integer (`Int64`) | count | Number of websites whose feature has code 0 | 0 to 11,055 | None observed | [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `1 Count` | integer (`Int64`) | count | Number of websites whose feature has code 1 | 0 to 11,055 | None observed | [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `Total Websites` | integer (`UInt32`) | count | Number of websites in each URL-length, subdomain, or SSL category | 0 to 11,055 | None observed | [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `Phishing Websites` | integer (`UInt32`) | count | Number with `Result = -1` in each category | 0 to 4,898 | None observed | [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `Phishing Percentage` | float (`Float64`) | percent | 100 × phishing websites / total websites in the category, rounded to two decimals | 0 to 100 | None observed | [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `len` | integer (`UInt32`) | count | Number of rows in a Polars group | 0 up to the source dataframe’s row count | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) and [primary EDA](notebooks/eda_primary_phishing_websites.ipynb) |
| `percent` | float (`Float64`) | percent | Share of all PhiUSIIL rows in a class, or share of a class in a subdomain group | 0 to 100 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `rows` | integer (`UInt32`) | count | Rows per URL or per class in audit and comparison summaries | 0 to 235,795 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `labels` | integer (`UInt32`) | count | Number of distinct labels for each URL | Observed 1 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), `url_groups` |
| `class_rows` | integer (`UInt32`) | count | Total number of rows in a PhiUSIIL class | 100,945 or 134,850 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `present_rows` | integer (`Int64`) | count | Number of rows with a selected binary feature equal to 1 | 0 to 235,795 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), `binary_summary` |
| `present_pct` | float (`Float64`) | percent | 100 × `present_rows` / total PhiUSIIL rows | 0 to 100 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `unique_URLs` | integer (`UInt32`) | count | Rows per class after keeping the first occurrence of each URL for the temporary check | 0 to 235,370 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `stored_length_median` | float (`Float64`) | characters | Median publisher-recorded URL length | Nonnegative number | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `text_length_median` | float (`Float64`) | characters | Median URL length calculated from the text | Nonnegative number | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `length_median` | float (`Float64`) | characters | Median publisher-recorded URL length in the temporary deduplicated table | Nonnegative number | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `stored_HTTPS_pct` | float (`Float64`) | percent | Percentage with `IsHTTPS = 1` | 0 to 100 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `scheme_HTTPS_pct` | float (`Float64`) | percent | Percentage with `HTTPSFromURL = 1` | 0 to 100 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `HTTPS_pct` | float (`Float64`) | percent | Percentage with `IsHTTPS = 1` in the temporary deduplicated table | 0 to 100 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `password_field_pct` | float (`Float64`) | percent | Percentage with `HasPasswordField = 1` in the temporary deduplicated table | 0 to 100 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `external_form_pct` | float (`Float64`) | percent | Percentage with `HasExternalFormSubmit = 1` in the temporary deduplicated table | 0 to 100 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section B |
| `check` | string | N/A | Name of an audit check | Check names defined in Section B | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `affected_rows` | integer (`Int64`) | count | Number of rows flagged by an audit check; checks can overlap | 0 to 235,795 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `feature` | string | N/A | Name of the numeric or binary feature being summarized | Names in `selected_numeric` or `binary_features` | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `column` | string | N/A | Original column name in the transposed profile or null-count display | The 56 PhiUSIIL column names | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section A |
| `statistic` | string | N/A | Statistic name in `df.describe()` | `count`, `null_count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`, `max` | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section A |
| `null_count` | integer (`UInt32`) or string | count | Missing-value count; shown as text in the transposed profile | Observed 0 | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section A |
| `count` | integer (`int64`) or string | count | Rows included in a pandas summary or frequency series; shown as text in the transposed PhiUSIIL profile | Nonnegative count | None observed | [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb), [secondary EDA](notebooks/eda_secondary.ipynb), and [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `mean` | float (`Float64`/`float64`); string in the transposed profile | Same as summarized feature | Arithmetic mean of the feature in the stated dataset/class/group | Depends on the feature; numeric values are nonnegative in these analyses | None in numeric analysis summaries; profile has nulls for nonnumeric mean | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) and [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `std` | float (`Float64`/`float64`); string in the transposed profile | Same as summarized feature | Sample standard deviation of the feature in the stated dataset/class/group | Depends on the feature; numeric values are nonnegative in these analyses | None in numeric analysis summaries; profile has nulls for nonnumeric std | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) and [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `min` | float (`Float64`/`float64`); string in the transposed profile | Same as summarized feature | Minimum of the feature in the stated dataset/class/group | Depends on the feature; numeric values are nonnegative in these analyses | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) and [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `max` | float (`Float64`/`float64`); string in the transposed profile | Same as summarized feature | Maximum of the feature in the stated dataset/class/group | Depends on the feature; numeric values are nonnegative in these analyses | None observed | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) and [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `median` | float (`Float64`/`float64`) | Same as summarized feature | Median of the feature in the stated dataset/class/group | Depends on the feature; numeric values are nonnegative in these analyses | None in numeric analysis summaries | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) and [checkpoint notebook](notebooks/eda_checkpoint_three.ipynb) |
| `q25` | float (`Float64`/`float64`) | Same as summarized feature | 25th percentile of the feature in the stated dataset/class/group | Depends on the feature; numeric values are nonnegative in these analyses | None in numeric analysis summaries | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `q75` | float (`Float64`/`float64`) | Same as summarized feature | 75th percentile of the feature in the stated dataset/class/group | Depends on the feature; numeric values are nonnegative in these analyses | None in numeric analysis summaries | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `p99` | float (`Float64`/`float64`) | Same as summarized feature | 99th percentile of the feature in the stated dataset/class/group | Depends on the feature; numeric values are nonnegative in these analyses | None in numeric analysis summaries | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb) |
| `25%` | string in the transposed profile | Same as summarized feature | 25th percentile displayed in the profile | Text form of the numeric statistic | Null for nonnumeric source columns | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section A |
| `50%` | string in the transposed profile | Same as summarized feature | Median displayed in the profile | Text form of the numeric statistic | Null for nonnumeric source columns | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section A |
| `75%` | string in the transposed profile | Same as summarized feature | 75th percentile displayed in the profile | Text form of the numeric statistic | Null for nonnumeric source columns | [PhiUSIIL EDA](notebooks/eda_phiusiil.ipynb), Section A |

In PhiUSIIL's `class_binary` summary, `IsHTTPS`, `HasObfuscation`, `IsDomainIP`, `NoOfURLRedirect`, `HasPasswordField`, and `HasExternalFormSubmit` keep their original names but become `Float64` percentages (0 to 100) within each class. They have no nulls. They are calculated as 100 × the class mean in [eda_phiusiil.ipynb](notebooks/eda_phiusiil.ipynb), Section D, rather than being new source features. In the one-row null-check tables, the source column names instead hold `UInt32` missing-value counts, all zero.

The secondary crosstabs use the original IP, SSL, or URL-length codes as their row index. The pivots use `ip_feature` or `length_group` as the index. A zero in a count or percentage table means no rows in that category, not missing data. The profile's null statistics for text columns mean the statistic does not apply; they do not mean the source rows are missing.

---

# 4. Reproduction Recipe

## Before running the notebooks

Use Python 3 and install the packages our notebooks use:

```bash
python -m pip install jupyterlab polars pandas scipy numpy matplotlib ipython liac-arff
cd notebooks
python -m jupyterlab
```

Run each notebook from top to bottom in a fresh kernel, with `notebooks/` as the working directory. The `arff` import in our Polars notebooks comes from **liac-arff**, while the pandas notebooks use `scipy.io.arff`. We did not save the original package versions in a dependency lockfile.

The three UCI files below are already in the repository. A source check on October 28, 2026 found that UCI 967 and 327 match the public downloads byte for byte. UCI 379 differs only in line endings; its column names, row order, and values match. If a file is missing, download and unzip it from the publisher, then save it at the path listed below. These files contain features the researchers already extracted. We did not collect the original webpages or HTML, or extract those features again.

## Primary 1: PhiUSIIL Phishing URL (UCI 967)

1. **Download:** Use the [UCI dataset page](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset) or its [download ZIP](https://archive.ics.uci.edu/static/public/967/phiusiil%2Bphishing%2Burl%2Bdataset.zip). The raw filename is `PhiUSIIL_Phishing_URL_Dataset.csv`. Keep it at [datasets/PhiUSIIL_Phishing_URL_Dataset.csv](datasets/PhiUSIIL_Phishing_URL_Dataset.csv).
2. **Load:** [phishing_urls.ipynb](notebooks/phishing_urls.ipynb) loads the CSV with `pl.read_csv`. [eda_phiusiil.ipynb](notebooks/eda_phiusiil.ipynb) loads the same file to check and analyze the data. Polars reads the columns as 5 string, 41 integer, and 10 float columns. We keep all original columns, names, and label values (`0` phishing, `1` legitimate).
3. **Prepare:** In `eda_phiusiil.ipynb`, Section B creates a separate `audit` dataframe with `URLTextLength` (character length of `URL`) and integer `HTTPSFromURL` (whether the lowercased URL starts with `https://`). The checks for missing values, duplicates, unusual values, and feature disagreements do not change the data. We keep all rows, including the 850 rows with repeated URLs, 187,151 stored-length disagreements, and 493 HTTPS disagreements. The temporary `dedup` table keeps the first occurrence of each URL only to check whether repeated URLs affect the results. Section D creates `subdomains` with `subdomain_group`: `0`, `1`, `2`, or `3+`, using the original `NoOfSubDomain`. In [eda_checkpoint_three.ipynb](notebooks/eda_checkpoint_three.ipynb), `pd.read_csv` loads a separate copy, and `pd.cut` adds `length_group` with bins `(0, 25]`, `(25, 40]`, and `(40, infinity]`. We do not drop rows, fill in missing values, or correct values in the main analysis.
4. **Dimensions:** Running those cells gives **235,795 × 56** for the main `df`, **235,795 × 58** for `audit`, **235,370 × 58** for the temporary `dedup` table (425 extra URL occurrences removed), and **235,795 × 57** for `subdomains`. The checkpoint notebook's `primary_df` ends at **235,795 × 57** after adding `length_group`. These columns are added to separate copies of the data.
5. **Joins/comparisons:** No secondary dataset is joined to PhiUSIIL. The checkpoint notebook and [eda_secondary.ipynb](notebooks/eda_secondary.ipynb) compare summaries calculated separately for each dataset. There is one internal join in `eda_phiusiil.ipynb`: the seven label/subdomain-group counts join to the two class totals on `label`, using Polars' default inner join. All **7** left summary rows match, **0** are unmatched, and both class totals are used; `subdomain_rates` is **7 × 5**. We use these class totals to calculate percentages within PhiUSIIL.

## Primary 2: Phishing Websites (UCI 327)

1. **Download:** Use the [UCI dataset page](https://archive.ics.uci.edu/dataset/327/phishing) or its [download ZIP](https://archive.ics.uci.edu/static/public/327/phishing%2Bwebsites.zip). The raw filename is `Training Dataset.arff`, stored at [datasets/phishing-websites/Training Dataset.arff](datasets/phishing-websites/Training%20Dataset.arff). Use this file, not the separate `.old.arff` release file.
2. **Load:** [phishing_websites_exploration.ipynb](notebooks/phishing_websites_exploration.ipynb) and [eda_primary_phishing_websites.ipynb](notebooks/eda_primary_phishing_websites.ipynb) read the ARFF using `arff.load`, take column names from `dataset["attributes"]`, and build a Polars dataframe from `dataset["data"]` with `orient="row"`.
3. **Prepare:** Both notebooks convert every column from string codes to `pl.Int64` integers. The `Result` codes stay the same (`-1` phishing, `1` legitimate). The exploration notebook keeps the original column names. The EDA notebook renames `Shortining_Service` to `Shortening_Service` and `Domain_registeration_length` to `Domain_registration_length`. We use grouped counts and percentages in the EDA. We do not remove rows, fill missing values, or add features to the main dataframe. Dropping `Result` to make the plotting variable `features` does not drop it from `df`.
4. **Dimensions:** After loading and converting the values to integers, `df` is **11,055 × 31**. We keep all 11,055 rows, and there are no nulls. The feature-only plotting copy is **11,055 × 30**.
5. **Joins/comparisons:** The last code cell in `eda_primary_phishing_websites.ipynb` separately loads UCI 379 into `df_secondary` (**1,353 × 10**) and converts only its `SSLfinal_State` column to `Int64`. It compares the percentages in each SSL category across the two datasets. No records are merged, and there is no join key, join type, or matched/unmatched row count.

## Secondary: Website Phishing (UCI 379)

1. **Download:** Use the [UCI dataset page](https://archive.ics.uci.edu/dataset/379/website+phishing) or its [download ZIP](https://archive.ics.uci.edu/static/public/379/website%2Bphishing.zip). The raw filename is `PhishingData.arff`, stored at [datasets/website-phishing/PhishingData.arff](datasets/website-phishing/PhishingData.arff).
2. **Load:** [website_phishing_secondary.ipynb](notebooks/website_phishing_secondary.ipynb) uses `arff.load` and builds a Polars dataframe with the attribute names. The codes are still strings at this stage. For analysis, [eda_secondary.ipynb](notebooks/eda_secondary.ipynb) uses `scipy.io.arff.loadarff`, builds a pandas dataframe, decodes object columns from UTF-8 bytes, then runs `df.astype(int)`. [eda_checkpoint_three.ipynb](notebooks/eda_checkpoint_three.ipynb) loads the data the same way with pandas.
3. **Prepare:** The main EDA keeps all three `Result` classes: 702 phishing (`-1`), 103 suspicious (`0`), and 548 legitimate (`1`). We keep the 629 duplicate feature/classification rows because there are no website IDs to tell us whether they are the same websites. There are no missing values to fill and no new columns in the main table. Only the checkpoint notebook's IP comparison creates `secondary_binary`, keeping `Result` in `[-1, 1]` and excluding the 103 suspicious rows.
4. **Dimensions:** The full analysis dataframe is **1,353 × 10**, with no rows dropped. The temporary binary comparison is **1,250 × 10**, keeping all 702 phishing and 548 legitimate rows.
5. **Joins/comparisons:** We do not join individual rows from the primary and secondary datasets. The checkpoint notebook groups PhiUSIIL by `IsDomainIP` and `secondary_binary` by `having_IP_Address`, calculates each dataset's phishing rates, renames the summary keys to `ip_feature`, and adds a `dataset` label. `pd.concat` stacks two **2 × 3** summaries into `ip_compare` (**4 × 3**); it does not match websites. The URL-length plots in `eda_secondary.ipynb` also use separate datasets. For these comparisons, join keys, join types, and matched/unmatched record counts are **not applicable**, rather than zero matches.

## Secondary: Tranco Top Sites

1. **Download:** Use the fixed [Y8YJG snapshot page](https://tranco-list.eu/list/Y8YJG) and [one-million-domain CSV endpoint](https://tranco-list.eu/download/Y8YJG/1000000). The download URL has no filename extension. Our notebook saves the file as `tranco_Y8YJG.csv` under `datasets/tranco/raw/`. This folder is excluded from Git, so someone starting with a fresh copy of the repository needs to download it. Use this snapshot rather than the changing latest list.
2. **Load:** [tranco_data_acquisition.ipynb](notebooks/tranco_data_acquisition.ipynb) creates the folder and downloads the file if it is missing. It reads the headerless CSV with `pl.read_csv`, assigning `rank: pl.Int64` and `domain: pl.String`.
3. **Prepare:** The notebook checks for nulls and repeated domains, then adds `domain_length` using character length, `number_of_dots` using a literal-dot regex, `contains_hyphen` using a literal `-` check, and `contains_number` using `[0-9]`. The two counts are `UInt32`, and the two indicators are boolean. We do not filter, drop, or relabel any rows. We do not use dot count as a subdomain count or label popular domains as legitimate.
4. **Dimensions:** Running the notebook with our local snapshot gives **1,000,000 × 2** before feature creation and **1,000,000 × 6** afterward. We keep all rows, with zero nulls and zero repeated domains. The local CSV's SHA-256 is `071ac7c36da7a7c10f8b415b1ab946d5d07088c55a789fc5ab38c76ad41da5fe`; compare a new download using `shasum -a 256 datasets/tranco/raw/tranco_Y8YJG.csv` from the repository root.
5. **Joins/comparisons:** The existing notebook stops after downloading the data, checking it, and adding the features. It does not join Tranco to PhiUSIIL or either ARFF dataset, and it does not yet run the proposed cross-dataset domain comparison. There are no join keys or matched/unmatched counts to report. The [publisher API](https://tranco-list.eu/api/lists/id/Y8YJG) confirms the snapshot dates and availability. A fresh download on October 28, 2026 matched the local CSV and the SHA-256 above.

---

# 5. Access and Reuse

The publisher pages and license terms below were checked on **October 28, 2026**. This is when we checked the documentation, not when we first downloaded the data. Download dates and release numbers we did not save are marked as undocumented.

| Dataset | Persistent source | Version or snapshot and access date | Original file format | Verified license or terms | Can we redistribute our processed data? |
|---|---|---|---|---|---|
| PhiUSIIL Phishing URL, UCI 967 | [UCI record](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset); [Mendeley dataset DOI](https://doi.org/10.17632/shwpxscxy2.2) | Mendeley v2, published November 15, 2023. Section 1 records project access on October 26, 2026. We did not save release details showing whether our local UCI CSV is exactly the same file as Mendeley v2. | CSV | CC BY 4.0, listed by both [UCI](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset) and [Mendeley](https://data.mendeley.com/datasets/shwpxscxy2/2). | Yes, under CC BY 4.0. Credit Arvind Prasad and Shalini Chandra, link the source and license, and describe our changes. |
| Phishing Websites, UCI 327 | [Dataset DOI](https://doi.org/10.24432/C51W2X) | UCI donation: March 25, 2015; numbered release and original project access date not documented. Publisher checked October 28, 2026. | ARFF, inside ZIP | CC BY 4.0, listed on the [UCI publisher page](https://archive.ics.uci.edu/dataset/327/phishing). | Yes, under CC BY 4.0. Credit Rami Mohammad, Fadi Thabtah, and Lee McCluskey, link the source and license, and describe our changes. |
| Website Phishing, UCI 379 | [Dataset DOI](https://doi.org/10.24432/C5B301) | UCI donation: November 1, 2016; numbered release and original project access date not documented. Publisher checked October 28, 2026. | ARFF, inside ZIP | CC BY 4.0, listed on the [UCI publisher page](https://archive.ics.uci.edu/dataset/379/website+phishing). | Yes, under CC BY 4.0. Credit Neda Abdelhamid, link the source and license, and describe our changes, including the temporary binary filter when sharing that subset. |
| Tranco Top Sites | [Snapshot Y8YJG](https://tranco-list.eu/list/Y8YJG) | Our [README](README.md) records generation on September 26, 2026, using August 28 to September 26 rankings, and download on September 27, 2026. Local download metadata also records September 27. The [publisher API](https://tranco-list.eu/api/lists/id/Y8YJG) confirms the generation date and ranking window; a fresh download matched our local CSV on October 28, 2026. | Headerless CSV | A license allowing us to redistribute this combined snapshot is **unverified**. The [Tranco publisher's attribution notice](https://tranco-list.eu/) lists upstream Majestic CC BY 3.0, CrUX CC BY-SA 4.0, and Cloudflare Radar CC BY-NC 4.0 terms; Cisco is described as free of charge, and no Farsight license is stated there. | **Not confirmed.** We need to confirm the snapshot's terms before sharing the raw or processed ranking. For now, share the fixed source link and preparation code. |

For the UCI datasets, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) allows sharing and adaptation, including commercial reuse. We need to keep the supplied notices, credit the creators, link the license, and describe our changes. We also cannot add restrictions that prevent uses the license allows. Being able to download Tranco does not mean we have permission to redistribute it. Its source datasets' terms alone do not confirm a license for the combined snapshot.

## FAIR assessment

- **Findable:** The UCI records and dataset DOIs identify the three phishing datasets. Tranco's fixed snapshot ID points to the list we used instead of the changing daily list.
- **Accessible:** The UCI tables have public downloads and repository copies. Tranco's notebook has a public download URL, but its local files are excluded from Git and are not included in a fresh copy of the repository. A fresh download of the fixed snapshot was verified on October 28, 2026.
- **Interoperable:** CSV and ARFF can be read with common Python libraries. Our notebooks show the type conversions. Similar feature names do not always mean the same measurement, and the two ARFF datasets lack URLs or domain IDs for matching individual records. We keep their class codes separate from PhiUSIIL's codes.
- **Reusable:** The UCI licenses allow reuse with attribution, and Section 4 records our preparation steps. We did not save the original package versions or complete download/version records, and we do not have the original webpages. Tranco's snapshot terms still need confirmation, and its popular domains are not verified legitimate examples. The secondary Website Phishing table also includes a suspicious class and repeated feature combinations. Anyone removing these should explain that choice.

---

# 6. People and Potential Impact

### People Represented or Affected by the Data

Our primary two datasets contain information about phishing and legitimate websites rather than individual people. They include URL and webpage characteristics, such as URL length, HTTPS usage, domain information, and redirects. Neither measures people's demographics. 

However, people can still be indirectly represented or affected by how these datasets are used. For example, people who browse websites in different languages, regions, or online environments may encounter different types of phishing attempts. Since our datasets do not include demographic information, we can't determine whether certain groups are represented or whether our findings apply equally to everyone.

### Applying the CARE Principles

- **Collective Benefit:** Our research could benefit internet users by identifying URL and webpage features that phishing websites share with legitimate websites. These findings could bring more awareness to phising and which methods are harder to distinguish. 

- **Authority to Control:** Although our datasets are publicly available, the individuals and website owners associated with the URLs may not have had direct control over how their website information was collected or reused. We should be mindful of how we use and share this information.

- **Responsibility:** We have a responsibility to accurately interpret our findings and acknowledge the limitations of our datasets. Since the data does not measure human recognition, we should avoid claiming that certain features directly cause people to fall for phishing attempts.

- **Ethics:** We should consider the potential consequences of our findings, including the possibility of legitimate websites being incorrectly identified as phishing websites. We should also avoid sharing potentially harmful phishing links unnecessarily and be careful not to present our results as applicable to all websites or users.