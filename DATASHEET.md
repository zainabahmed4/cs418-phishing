# Data Documentation

## Dataset Inventory

### Primary Datasets

1. **PhiUSIIL Phishing URL (Website)** — UCI #967
2. **Phishing Websites** — UCI #327

### Secondary Datasets

1. **PhishTank**
2. **Tranco Top Sites**

---

# 1. Primary Dataset Datasheets

## Primary Dataset #1: PhiUSIIL Phishing URL (Website)

Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset)  

Dataset version: Version 2 on Mendeley Data

Dataset DOI: 10.17632/shwpxscxy2.2

### 1. Motivation  

The PhiUSIIL dataset was created to help researchers study and detect phishing websites, which are fake or misleading websites that try to look trustworthy so that users will click on them or give away information such as passwords or financial info. They wanted to build a large dataset that included both phishing and legit websites and many different characteristics of their URLs and webpages. These features could then be used to train and test machine learning models for phishing detection. The dataset was created by Arvind Prasad and Shalini Chandra. According to the research paper, the authors didn't receive funding or support from an organization for this work.

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

Legitimate URLs were collected by the researches, then downloaded the webpages and extracted information from the URL and webpage source code to create the dataset features. UCI states that most of the URLs used to create the dataset were recent URLs at the time the dataset was constructed.

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
- Latest access date for our project: October 26, 2026  
- The CC BY 4.0 license allows other people to share and adapt the dataset as long as they give proper credit to the original creators.

### 7. Maintenance  

The dataset is currently hosted by both the UCI Machine Learning Repository and Mendeley Data. The Mendeley record shows that there have been at least two published versions. Version 1 was published on August 29, 2023, and Version 2 was published on November 15, 2023. Version 2 is the latest version currently listed on Mendeley. UCI lists the dataset as donated on March 3, 2024. A regular schedule for future updates is not documented by the publisher. Someone reusing the dataset in the future could try checking the UCI page and the Mendeley version history to see whether a newer version has been released.

---

## Primary Dataset #2: Phishing Websites

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/327/phishing)

**Dataset DOI:** https://doi.org/10.24432/C51W2X

### 1. Motivation

The Phishing Websites dataset was created to help researchers identify which website characteristics are useful for identifying phishing websites from legit websites. The researchers explained that reliable training datasets for phishing detection were difficult to find, so they wanted to provide a dataset containing important phishing-related features and introduce additional features that could improve phishing detection.

The dataset was created by Rami Mohammad and Lee McCluskey.

**Funding:** Not documented by the publisher.

**Sources:**
- [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)
- [University of Huddersfield Dataset Record](https://eprints.hud.ac.uk/id/eprint/24330/)

### 2. Composition

The Phishing Websites dataset contains **11,055 rows and 31 columns** (30 features and 1 classification column).

Each row represents one website with features related to its URL, domain, security, and webpage characteristics. The `Result` column identifies whether a website is phishing (-1) or legitimate (1).

- **Phishing websites:** 4,898
- **Legitimate websites:** 6,157
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



---

# 3. Codebooks

## PhiUSIIL

## PhiUSIIL Codebook

The table below documents the PhiUSIIL columns that we used in our exploratory analysis, along with the additional columns we created during analysis. The original dataset contains more columns, but we only included the ones that were actually used in our project so far.

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


## Phishing Websites

[PRIMARY #2 CODEBOOK]

## Secondary Dataset Variables Used



---

# 4. Reproduction Recipe



---

# 5. Access and Reuse



---

# 6. People and Potential Impact

