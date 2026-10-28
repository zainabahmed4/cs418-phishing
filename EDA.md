# Exploratory Data Analysis

**Current group research question:** Which URL and webpage features are shared by both phishing and legitimate websites, potentially making them harder to distinguish?

**Original research question:** Which features of phishing links and webpages make them harder for people to recognize?

## 1. Profile each dataset

### PhiUSIIL primary dataset

The PhiUSIIL dataset has **235,795 rows and 56 columns** (`df.shape == (235795, 56)`). Looking at `df.glimpse()`, there are 5 string columns (`FILENAME`, `URL`, `Domain`, `TLD`, and `Title`), 41 integer columns, and 10 float columns. `FILENAME` identifies the records, while `label` tells us whether a website is legitimate (`1`) or phishing (`0`). The other columns describe things like the URL, domain, HTTPS, webpage content, forms, and redirects. I kept the original column names, even when they have spelling mistakes, like `NoOfDegitsInURL` and `SpacialCharRatioInURL`.

One thing that stood out from `df.null_count()` is that **none of the 56 columns have missing values**. Looking at `df.describe()`, URL lengths vary a lot: the median `URLLength` is 27, but the maximum is 6,097. The same goes for `LineOfCode`, which has a median of 429 and a maximum of 442,666. `DomainLength` doesn't vary as much, with a median of 20, a middle 50% between 16 and 24, and a maximum of 110. There are **134,850 legitimate websites (57.2%)** and **100,945 phishing websites (42.8%)**. Since the groups aren't exactly the same size, we'll use percentages when comparing them rather than relying only on counts.

**Notebook:** [eda_phiusiil.ipynb](./notebooks/eda_phiusiil.ipynb), dataset profiling section.

### Phishing Websites primary dataset

The Phishing Websites ARFF dataset has **11,055 rows and 31 columns** (`df.shape == (11055, 31)`). Thirty columns describe website characteristics, and the last column, `Result`, tells us whether the website is phishing (`-1`) or legitimate (`1`). The feature values are categories, usually `-1`, `0`, or `1`, rather than actual measurements. After converting the columns, `df.glimpse()` shows them as `i64`. The EDA renames `Shortining_Service` to `Shortening_Service` and `Domain_registeration_length` to `Domain_registration_length`; the exploration notebook keeps the source names.

There are **no missing values** according to `df.null_count()`. Since the features use categorical codes, the means and standard deviations from `df.describe()` aren't very useful for interpreting them. What's more useful is counting how often each category appears. There are **6,157 legitimate websites** and **4,898 phishing websites**. Another thing I noticed is that `Redirect` only uses 0 and 1. From the distribution graphs, `URL_Length` has 8,960 rows in the -1 category, `Prefix_Suffix` has 9,590 in -1, `having_At_Symbol` has 9,400 in 1, and `SSLfinal_State` has 6,331 in 1.

**Notebook:** [eda_primary_phishing_websites.ipynb](./notebooks/eda_primary_phishing_websites.ipynb), dataset profiling section.

### UCI Website Phishing secondary dataset

Our secondary dataset is smaller, with **1,353 rows and 10 columns** (`df.shape == (1353, 10)`). Nine columns describe website features: `SFH`, `popUpWidnow`, `SSLfinal_State`, `Request_URL`, `URL_of_Anchor`, `web_traffic`, `URL_Length`, `age_of_domain`, and `having_IP_Address`. The tenth column is `Result`. The values originally loaded as strings, so they had to be converted to integers before we could analyze them.

There are **no missing values** according to `df.isnull().sum()`. Unlike the primary Phishing Websites dataset, this one has three result categories: **702 phishing, 548 legitimate, and 103 suspicious**. Some features allow -1, 0, and 1, while `age_of_domain` and `having_IP_Address` use two values. The suspicious class is much smaller than the other two, which is something to keep in mind when comparing percentages.

**Notebook:** [eda_secondary.ipynb](./notebooks/eda_secondary.ipynb), dataset profile section.

## 2. Anything unusual in the data?

### PhiUSIIL

The checks in [eda_phiusiil.ipynb](./notebooks/eda_phiusiil.ipynb) didn't find any nulls, blank values, invalid binary codes, nonfinite numbers, out-of-range ratios, or URL parsing failures. However, a few things stood out that we wanted to keep track of instead of changing the original data.

| What we noticed | How many rows? | What we decided |
|---|---:|---|
| Repeated URLs | 850 rows, covering 425 URLs that appear twice | Kept them. The records have different filenames/features but the same labels, and we don't know which observation should be preferred. |
| `URLLength` doesn't match the length of the displayed URL | 187,151 | Kept the stored length and flagged the difference. Most are off by one character, but we can't confirm exactly why. |
| `IsHTTPS` doesn't match the URL scheme | 493 | Flagged them. These have HTTP URLs but `IsHTTPS = 1` and `label = 0`. We don't know the original extraction context. |
| Possible issues with title text encoding | 8 | Flagged rather than guessing how to fix the text. |
| Extra spaces around a title | 1 | Kept and flagged. |
| `Title = "0"` and `HasTitle = 0` | 32,714 | Kept as a marker for no title rather than treating it as a missing value. |
| `Title = "0"` but `HasTitle = 1` | 5 | Flagged because the meaning is unclear. |
| `Title = "na"` but `HasTitle = 1` | 5 | Kept and flagged instead of assuming the title is missing. |
| Extremely long URLs or webpages | 2,350 URLs and 2,357 webpages above their respective 99th-percentile cutoffs | Kept them. Being an extreme value doesn't automatically mean it's wrong; we used log-scaled plots where helpful. |

There were also **no completely identical rows**. Two URLs have uppercase characters, but since capitalization can matter in URL paths, we didn't change them. We also checked what happened when keeping only the first occurrence of repeated URLs, and the percentages were almost unchanged, so we kept the original rows.

### Phishing Websites primary dataset

The values originally loaded as strings, even though they represent integers, so they were converted to `Int64`. There are **no missing values**, and the feature values are within the expected -1, 0, and 1 categories. `Redirect` only uses 0 and 1, but that isn't something we need to fix. We corrected the two column spellings listed above and did not remove any rows. The final data check found 5,206 repeated feature/classification rows, which we kept because no website IDs are provided.

### UCI secondary dataset

The secondary dataset has **629 duplicate rows** and no missing values. Since we don't have a website ID, we can't tell whether the duplicates are the same website or different websites with the same features. Because of that, we kept them and noted it as a limitation. We also converted the string values into integers. No rows had values outside the documented categories, and we didn't remove any data.

## 3. Looking at the distributions

These graphs show how often a feature value appears, but **they don't tell us whether that feature is associated with phishing until we compare it against the result/classification**.

### PhiUSIIL

`URLLength` is very right-skewed. Most URLs are much shorter, with a median of 27 and the middle 50% between 23 and 34, but the longest URL is 6,097 characters. `DomainLength` is more concentrated. For `NoOfSubDomain`, 178,406 websites (75.7%) have a value of 1, although the values go up to 10. `SpacialCharRatioInURL` is centered around 0.05, with the middle 50% between 0.038 and 0.083, and a maximum of 0.397. `LineOfCode` also has some very large values, so we used a log scale to make the distribution easier to see. Another thing that stood out was that HTTPS is common (78.26%), while URL obfuscation (0.21%) and IP-based domains (0.27%) are rare.

**Notebook:** [eda_phiusiil.ipynb](./notebooks/eda_phiusiil.ipynb), feature distributions.

### Phishing Websites primary dataset

The distributions for `URL_Length`, `having_At_Symbol`, `Prefix_Suffix`, `SSLfinal_State`, and `HTTPS_token` are pretty unbalanced, with one category appearing much more frequently than the others. `having_Sub_Domain` is a little different: 3,363 websites have a value of -1, 3,622 have 0, and 4,070 have 1. Those three categories are much closer together. Since these numbers are categories, rather than actual measurements, describing numerical skew or outliers wouldn't really make sense here.

**Notebook:** [eda_primary_phishing_websites.ipynb](./notebooks/eda_primary_phishing_websites.ipynb), distribution graphs.

### UCI secondary dataset

The secondary dataset has more phishing websites (702) than legitimate (548) or suspicious (103). Looking at its feature distributions, `having_IP_Address` is mostly 0, while `SSLfinal_State` and `SFH` have a lot of 1s. `URL_of_Anchor` has more -1s and 1s than 0s, and `web_traffic` is more evenly distributed. Again, this tells us which values are common, but we need to compare them to `Result` to understand their relationship to phishing.

**Notebook:** [eda_secondary.ipynb](./notebooks/eda_secondary.ipynb), distribution graphs.

## 4. Relationships between features and classification

### Plot 1 – URL Length and Domain Structure vs. Result

In PhiUSIIL, phishing websites have a median URL length of **34** characters (middle 50%: 26–48), compared to **26** (23–29) for legitimate websites. Domain names are also a little longer for phishing websites, with medians of **22** and **19** respectively. In our other primary dataset, the percentage of phishing websites changes depending on the `URL_Length` category. The secondary dataset shows another pattern: about **42%** of websites in its -1 URL-length category are phishing, compared to around **59%** in category 1.

**So what?** I expected phishing URLs to be longer on average, and the PhiUSIIL data does show that. But the URL lengths overlap a lot between phishing and legitimate websites. That means length alone isn't enough to tell us whether a website is phishing. Another thing to keep in mind is that PhiUSIIL measures the actual URL length, while the other two datasets use categories, so we can't compare those numbers directly.

**What next?** I would want to compare URL length with domain length and see whether the relationship still holds. I'd also want to look specifically at phishing websites with normal-looking URL lengths and check whether they have other legitimate-looking characteristics, like SSL or subdomain features. For PhiUSIIL, we could check whether using the length calculated from the URL text changes anything.

**Notebooks:** [eda_phiusiil.ipynb](./notebooks/eda_phiusiil.ipynb), [eda_primary_phishing_websites.ipynb](./notebooks/eda_primary_phishing_websites.ipynb), and [eda_secondary.ipynb](./notebooks/eda_secondary.ipynb).

### Plot 2 – Subdomains and IP Address Features vs. Result

In PhiUSIIL, having one recorded subdomain is common for both phishing and legitimate websites, but it appears in **63.0% of phishing** websites compared to **85.2% of legitimate** websites. Having three or more subdomains is less common, appearing in 5.3% of phishing websites and 1.3% of legitimate ones. Something that surprised me is that all **13,983** websites recorded as having zero subdomains were phishing. That could be related to how the dataset counts subdomains, so it's worth checking before drawing a conclusion. In the secondary dataset, websites with an IP-address feature value of 1 have a phishing rate of about **59%**, compared to about **51%** for value 0. The cross-dataset analysis found that, in PhiUSIIL, all **638** rows with `IsDomainIP = 1` were phishing, while the Website Phishing secondary dataset had a smaller difference of around 65% versus 55% after excluding the 103 suspicious rows.

**So what?** I expected unusual domain structures or IP-based URLs to be related to phishing, and some of the results support that. What I didn't expect was for every website in the zero-subdomain group to be phishing, or for every IP-based domain in PhiUSIIL to be phishing. However, these patterns depend on how the features were defined and how many websites were in each group. The IP-based group is also quite small compared to the full dataset, so we shouldn't treat it as something that identifies most phishing websites.

**What next?** I'd want to check exactly how each dataset defines subdomains and IP-based URLs, ideally by looking at actual URL examples. Then we could look at whether these patterns change when we separate websites by HTTPS, URL length, or domain length.

**Notebooks:** [eda_phiusiil.ipynb](./notebooks/eda_phiusiil.ipynb), [eda_secondary.ipynb](./notebooks/eda_secondary.ipynb), and [eda_checkpoint_three.ipynb](./notebooks/eda_checkpoint_three.ipynb).

### Plot 3 – SSL/HTTPS and Webpage Features vs. Result

In the Phishing Websites primary dataset, **98.20%** of websites with `SSLfinal_State = 0` were phishing, compared to **85.77%** for -1 and **11.07%** for 1. What's interesting is that **701 phishing websites still had an SSL value of 1**, which is the category associated with legitimate websites. Comparing the primary and secondary datasets, category 1 was the most common in both. However, the secondary dataset had more websites in category 0 (**21.73% versus 10.56%**), while the primary had more in -1 (**32.18% versus 22.76%**). In PhiUSIIL, **49.22% of phishing** websites used HTTPS, compared to **100% of legitimate** websites. Obfuscation and IP-based domains only appeared among phishing websites in that dataset, but they were rare. Something I didn't expect was that password fields and external form submission were actually more common among legitimate websites (**13.85% vs. 5.39%**, and **7.37% vs. 0.43%**). Redirect rates were fairly close (**15.17% vs. 11.98%**).

**So what?** This is important for our research question because a phishing website can still have HTTPS or SSL features associated with legitimate sites. A security-related feature by itself doesn't prove a website is safe. I also thought forms would show up more often on phishing websites, so seeing more of them among legitimate websites was unexpected. It shows why we shouldn't assume one website characteristic always points to phishing.

**What next?** I'd want to look at phishing websites that have legitimate-associated SSL characteristics and see whether they also have normal-looking URL lengths or subdomains. We could also compare form features among HTTPS websites specifically. If we wanted to study whether people are actually fooled by these characteristics, we would need a separate study involving real users, since these datasets don't measure that.

**Notebooks:** [eda_phiusiil.ipynb](./notebooks/eda_phiusiil.ipynb), [eda_primary_phishing_websites.ipynb](./notebooks/eda_primary_phishing_websites.ipynb), and [eda_secondary.ipynb](./notebooks/eda_secondary.ipynb).

### Plot 4 – Special-Character Ratio vs. Result and URL Length

In the PhiUSIIL dataset, phishing URLs have a higher median `SpacialCharRatioInURL` (**0.080**) compared to legitimate URLs (**0.042**), and the values for phishing URLs are more spread out. This difference is still there when URLs are split into short, medium, and long groups. For short URLs, the medians are around 0.050 for phishing and 0.045 for legitimate; for medium URLs, 0.077 and 0.036; and for long URLs, 0.101 and 0.024. One thing to keep in mind is that the long-URL group has **36,066 phishing websites but only 798 legitimate ones**.

**So what?** I expected phishing URLs to have more unusual characters, and the data generally supports that. What's interesting is that the difference still appears even after separating URLs by length. However, the two groups still overlap, so we can't use this feature alone to identify every phishing URL. The long-URL results also need more caution because the groups are so different in size.

**What next?** Instead of only looking at the overall special-character ratio, I'd want to see which specific characters are responsible for the difference. I would also repeat the comparison just for medium-length URLs, where the groups are more balanced, and look at HTTPS websites separately.

**Notebook:** [eda_checkpoint_three.ipynb](./notebooks/eda_checkpoint_three.ipynb).

## 5. Overall – So what?

Looking at all four notebooks, I noticed a few patterns. Phishing websites generally have longer URLs, higher special-character ratios, and are more likely to show unusual domain or IP-address characteristics. Their SSL/HTTPS characteristics also differ from legitimate websites. A lot of this was what I expected, but some findings were surprising, especially seeing certain form-related features appear more often among legitimate websites.

What stood out to me most is that **phishing and legitimate websites share a lot of the same characteristics**. Some phishing websites still have normal-looking URL lengths, simple subdomain structures, or HTTPS/SSL features associated with legitimate websites. So I don't think we can point to just one feature and say it tells us whether a website is phishing. Looking at combinations of features would probably tell us more.

This also made me rethink our original research question. We originally asked which features make phishing links and webpages harder for people to recognize, but our datasets don't actually measure whether people can recognize phishing websites. They only tell us about website characteristics and classifications. I don't think we need to change the direction of our project, but I do think our wording should be more specific to what we're measuring.

**Revised research question:** Which URL and webpage features are shared by both phishing and legitimate websites, potentially making them harder to distinguish?

## 6. Overall – What's next?

Based on what we found, here's what I think we should look at next:

1. **Double-check how the features are defined.** Some variables, like IP-address indicators, subdomain counts, SSL categories, redirects, and URL length, aren't measured the same way across datasets. We should make sure we're interpreting them correctly.
2. **Compare more specific groups.** For example, we could look at only HTTPS websites or websites with similar URL lengths. We'd also want to include the number of websites behind each percentage so small groups don't make the results look more convincing than they are.
3. **Look at combinations of features.** I'm especially interested in whether phishing websites with legitimate-looking SSL characteristics also have normal URL lengths, simple subdomain structures, or fewer unusual characters.
4. **Be careful when comparing the datasets.** We can compare similar ideas across datasets, but we shouldn't join individual rows without matching website identifiers. The features and result labels aren't always defined in exactly the same way.
5. **Ask someone familiar with phishing detection about some of the unusual findings.** In particular, I'd want to understand why the form and webpage-related features behave differently than expected and whether that comes from the way the data was collected.
6. **Keep the human-recognition question separate.** If we eventually want to know whether these characteristics really fool people, we'd need data from a user study or an experiment. Our current datasets can't tell us that.

Overall, I think our revised research question fits what we're actually doing much better: **Which URL and webpage features are shared by both phishing and legitimate websites, potentially making them harder to distinguish?** The main reason for changing it is that our data measures website characteristics, not people's ability to recognize phishing. And so far, our results show that phishing websites can have several features we'd normally associate with legitimate ones.