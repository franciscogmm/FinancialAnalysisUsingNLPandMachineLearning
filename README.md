# FinancialAnalysisUsingNLPandMachineLearning
The purpose of this study is to explore whether the sentiment, structure, and contents of a company’s Proxy Statement Compensation Discussion and Analysis (CD&amp;A) reflects the company’s real financial performance in terms of the relationship of Earnings per Share and Operating Cash Flow per Share

## Hypothesis
In this project, we assumed that the more positive a company’s proxy statement’s CD&A was written, the better the earnings quality of a company is in a given fiscal year.

According to Investopedia, Two financial indicators are being used to present whether companies’ earnings with high quality or low quality. A company has high quality earnings if it is generating more cash than is reported in the income statement. Earning quality is low if the company’s statements are not showing the negative operating results of the company. True cash operating results are also overstated.

- High quality earnings: Earnings Per Share (EPS) > Operating Cash Flow Per Share (CFS)
- Low quality earnings: Earnings Per Share (EPS) < Operating Cash Flow Per Share (CFS)

## Data Description
- Randomly selected 1,500 companies’ S&P Proxy Statements’ Compensation Discussion and Analysis (CD&A) from the U.S.  SEC EDGAR System.
- Company performance (Earnings Per Share and Cash Flow Per Share) using the Intrinio Financial Marketplace API.
- Ticker and registered company industries from Google Finance.

In addition, two popular sentiment lexicons were selected for the sentiment analysis portion: Bing Liu’s sentiment dictionary and LoughranMcDonald Master Dictionary, which was specifically developed for Tim Loughran and Bill McDonald’s paper in the Journal of Finance entitled “When is Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks” (2011).

## Methodology
1. Data Preprocessing
  - Text data was extracted from the CD&As. It underwent cleaning, which involved removal of punctuations and special characters.
  - Domain-specific lexicon creation. In the process, positive and negative words, phrase, and templates were extracted from 200 of the 500 documents. In the process, positive and negative words, phrase, and templates were extracted.
  - Templates: e.g. an increase/decrease of amount from number>/year, metric increased/decreased amount over/compared to year
  - The team simulated “expertise” and classified the 200 documents into positive or negative performance/sentiment.
2. Sentiment Analysis
  - Feature-level Analysis
    - Polarity-based sentiment analysis was conducted using the two publicly available lexicons mentioned above.
    - Due to inadequate results, the team decided to create a new domain-specific lexicon that will hopefully produce a better result.
    - To complement the sentiment analysis, IBM Tone Analyzer was used to acquire 13 tonal dimension results for each company’s CD&A.
  - Document-level Analysis
    - Using the “expert” classifications of the 200 labeled data and the domain-specific lexicon as the feature set, a term-document matrix data set, containing the quantity/existence of each feature in all the documents (500 in total, was created.
    - Using a Neural Network, the remaining 300 documents were classified into positive or negative sentiment classes.
3. Classification of Earnings Quality
  - Considering the sentiment classification from the polarity-based sentiment analysis model, using the domain-specific dictionary and the tonal information as predictors and the earning quality as the target variable, four scenarios were used and subjected to multiple classification models (random forest, neural network, and logistic regression).
  - The following scenarios were tested:
    - Scenario 1 : Financial Performances ~ CD&A Tones
    - Scenario 2: Financial Performances ~ CD&A Sentiment
    - Scenario 3: Financial Performances ~ CD&A Tones + Sentiment
    - Scenario 4: Financial Performances ~ Top 5 Predictor Importance (Tone + Sentiment)
4. Tools:
  - R
  - Python
  - IBM Tone Analyzer
  
  
# Read the analysis at https://dataontherocks.wordpress.com/2017/06/04/classifying-a-companys-true-earnings-quality-using-text-analytics-and-machine-learning-on-sp-proxy-statements-compensation-discussion-and-analysis-r-python/
