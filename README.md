# CS 418 Research Project

### Which features of phishing links and webpages make them harder for people to recognize?


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
- **Time coverage:** A specific observation-level time span is not provided by UCI. The dataset was created around 2012 and donated to UCI in 2015
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

We will compare these popular domains with phishing URLs from PhiUSIIL and PhishTank. This will help us see whether features such as domain length, dot count, hyphens, and numbers differ between popular and phishing domains.

Group members: Srijani Prekki, Catherine Carter, Zainab Ahmed, Mehtab Kaur