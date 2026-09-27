# CS 418 Research Project

### Which features of phishing links and webpages make them harder for people to recognize?



## Dataset Notes:

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