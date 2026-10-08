# Secondary Dataset: Exploratory Data Analysis

## 1. Dataset Profile

The UCI Website Phishing dataset contains 1,353 rows and 10 columns. Nine columns represent phishing-related website features, and the `Result` column identifies whether a website is phishing, suspicious, or legitimate.

The dataset has no missing values. All columns were initially loaded as strings and were converted to integers for analysis.

The dataset contains:
- 702 phishing websites
- 103 suspicious websites
- 548 legitimate websites

## 2. Data Anomalies

| Anomaly | Rows affected | Action taken |
|---|---:|---|
| Repeated feature and classification combinations | 629 | Kept and flagged for further investigation |
| Missing values | 0 | No action needed |
| String data types | 1,353 | Converted to integers |
| Unexpected category codes | 0 observed | No action; valid categories should be checked against the source documentation |

The repeated rows were kept because multiple websites may share the same characteristics. Since the dataset does not contain unique website identifiers, we cannot confirm whether these represent duplicate websites.

## 3. Feature Distributions

The distribution plots showed that several features had uneven category frequencies.

- `SFH` and `SSLfinal_State` had more observations with a value of 1.
- `having_IP_Address` was mostly 0.
- `URL_Length` was most commonly 0.
- `web_traffic` had a relatively balanced distribution.
- `URL_of_Anchor` had fewer observations with a value of 0.

These differences show that certain website characteristics are more common than others. However, the category frequencies alone do not establish which features distinguish phishing websites.

*Source: `notebooks/eda_secondary.ipynb`, feature distribution plots.*

## 4. Relationships Between Features

### IP Address Feature vs. Website Classification

Websites with `having_IP_Address = 1` had approximately 59% phishing classifications, compared with 51% for websites with a value of 0.

**So what?** The IP address feature shows a moderate association with phishing classification, although neither category exclusively represents phishing websites.

**What next?** Compare the IP address feature with SSL status and other phishing indicators to determine whether combining features reveals stronger patterns.

### SSL Status vs. Website Classification

Approximately 74% of websites with `SSLfinal_State = 1` were classified as phishing, compared with 20% for websites with a value of -1.

**So what?** SSL status showed a larger difference between classification groups than IP address usage. The exact meaning of these category codes should be verified before interpreting the underlying security implications.

**What next?** Investigate whether SSL-related features show similar classification patterns in other phishing datasets.

### URL Length vs. Website Classification

Phishing classifications accounted for approximately 42% of category -1, 55% of category 0, and 59% of category 1.

**So what?** URL length-related categories appear associated with phishing classifications. However, the encoded categories are not actual character counts.

**What next?** Compare the findings with a dataset containing measured URL lengths.

*Source: `notebooks/eda_secondary.ipynb`, relationship plots.*

## 5. Cross-Dataset Comparison

The UCI Website Phishing dataset was compared with the primary PhiUSIIL Phishing URL Dataset.

The primary dataset contains 235,795 rows and 56 columns.

In the primary dataset:

| Measure | Phishing | Legitimate |
|---|---:|---:|
| Mean URL length | 45.72 | 26.23 |
| Median URL length | 34 | 26 |
| Maximum URL length | 6,097 | 57 |

Phishing URLs were generally longer and showed greater variation than legitimate URLs.

The secondary dataset also showed variation in phishing classification rates across URL length categories.

**So what?** Both datasets show associations between URL length-related characteristics and phishing classification. However, their measurements differ, so the numerical results should not be treated as directly equivalent.

**What next?** Investigate whether other indicators, such as IP address usage, show consistent relationships across datasets.

*Source: `notebooks/eda_secondary.ipynb`, cross-dataset URL length comparison.*

## 6. Research Questions and Next Steps

**Original research question:**

Which features of phishing links and webpages make them harder for people to recognize?

**Proposed revised research question:**

Which URL and webpage characteristics are associated with phishing classification, and do these relationships remain consistent across different phishing datasets?

The revised question focuses on patterns that can actually be measured using the available data. The datasets contain phishing-related website characteristics, but they do not directly measure whether people can recognize phishing websites.

Future analysis could examine combinations of features, compare additional datasets, and investigate which characteristics are most useful for distinguishing phishing websites from legitimate ones.

### Limitations

The secondary dataset uses categorical values rather than actual measurements for features such as URL length and SSL status. The exact meaning of each feature value must be verified using the original dataset documentation.

The analysis identifies relationships between website characteristics and phishing classifications, but these relationships do not prove causation. Also, the repeated feature combinations may represent different websites with similar characteristics rather than actual duplicate records.