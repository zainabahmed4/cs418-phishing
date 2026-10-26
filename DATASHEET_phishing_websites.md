# Primary Dataset 2: Phishing Websites

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/327/phishing)

**Dataset DOI:** https://doi.org/10.24432/C51W2X

## 1. Motivation

The Phishing Websites dataset was created to help researchers identify which website characteristics are useful for identifying phishing websites from legit websites. The researchers explained that reliable training datasets for phishing detection were difficult to find, so they wanted to provide a dataset containing important phishing-related features and introduce additional features that could improve phishing detection.

The dataset was created by Rami Mohammad and Lee McCluskey.

**Funding:** Not documented by the publisher.

**Sources:**
- [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)
- [University of Huddersfield Dataset Record](https://eprints.hud.ac.uk/id/eprint/24330/)

## 2. Composition

The Phishing Websites dataset contains **11,055 rows and 31 columns** (30 features and 1 classification column).

Each row represents one website with features related to its URL, domain, security, and webpage characteristics. The `Result` column identifies whether a website is phishing (-1) or legitimate (1).

- **Phishing websites:** 4,898
- **Legitimate websites:** 6,157
- **Missing values:** None
- **Data sources:** PhishTank, MillerSmiles, and Google search operators.

The dataset is a sample of websites from these sources, not every website on the internet.

**Limitations:** The dataset does not specify geographic coverage or exact collection dates. It also lacks unique website IDs, making it difficult to identify duplicate websites. Because the data comes from selected sources, it may not represent all websites.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

## 3. Collection Process

The dataset was collected mainly from PhishTank, MillerSmiles, and Google search operators. Researchers gathered phishing and legitimate websites and extracted features related to their URLs, domains, and webpage characteristics.

- **Collection method:** Online website records and automated feature extraction.
- **Time frame:** The dataset was submitted to UCI on March 25, 2015, but the exact collection dates are not documented by the publisher.
- **Consent:** The dataset describes websites rather than individual participants. Whether website owners were notified or gave consent is not documented by the publisher.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

## 4. Preprocessing

The researchers extracted phishing-related features from websites and converted them into numerical values such as -1, 0, and 1.

- **Cleaning:** Any additional cleaning or removal of records before publication is not documented by the publisher.
- **Missing values:** The published dataset has no missing values.
- **Raw data:** The extracted features are available in the `Training Dataset.arff` file, but the original website data used to create them is not provided.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

## 5. Uses

The dataset has been used in research to identify phishing websites and develop machine learning models for phishing detection.

Our group is using it to compare URL and webpage features associated with phishing across different datasets.

**Limitations:** The dataset should not be used to determine whether a person would recognize a phishing website. It also should not be used as the only method for detecting phishing because website characteristics and phishing techniques can change over time.

**Sources:**
- [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)
- [Predicting Phishing Websites Based on Self-Structuring Neural Network](https://eprints.hud.ac.uk/id/eprint/19220/)

## 6. Distribution

The dataset is available to the public through the UCI Machine Learning Repository. It can be downloaded as an ARFF file or accessed using Python's `ucimlrepo` package.

- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Reuse:** Others can copy, share, and modify the dataset as long as they give proper credit to the original creators.
- **Access:** Free and publicly available.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)

## 7. Maintenance

The dataset is hosted by the UCI Machine Learning Repository and was donated on March 25, 2015.

- **Maintenance:** UCI hosts the dataset, but who is responsible for maintaining its contents is not documented by the publisher.
- **Updates:** No regular update schedule is documented.
- **New versions:** Users can check the UCI dataset page for any changes or updates.

**Source:** [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/dataset/327/phishing)