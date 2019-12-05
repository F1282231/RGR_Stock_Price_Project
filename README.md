# RGR Stock Price Forecasting Project

Author: [Jack Wang](https://www.linkedin.com/in/jackweijiawang/)

---

## Problem Statement

Stock prices are hard to predict because they are not only affected by the performance of the underlying companies but also the expectations from the general public. As known, the stock price of firearm companies are highly correlated to the public opinions toward gun control. My model intends to predict the stock price of one of the largest firearm company in the states, RGR (Sturm, Ruger & Co., firearm company), by using its historical stock price, public opinions toward gun control, and its financial reports to SEC. 

## Executive Summary

The goal of my project is to build a **time series regression model** that predicts the stock price of RGR. The data I am using would be historical stock price from [Yahoo Finance](https://finance.yahoo.com/quote/RGR/history?p=RGR), twitter posts scraped from [twitter](https://twitter.com/), subreddit posts mentioned about gun control, and also the financial reports to [SEC](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000095029&type=&dateb=&owner=exclude&count=100). I will do sentiment analysis on the text data and time series modeling on the historical stock price data. The model will be evaluated using MSE.

## Software Requirements

Codes are written in Jupyter Notebook with Python. Users are recommended to know Python library `Numpy`, `Pandas`, time series models with `statsmodels.tsa` and `keras`, visualization with `matplotlib`, and the knowledge of ARIMA, SARIMAX, and neural networks.

## Dictionary

|Column Name|Type|Data Collected|Description|
|:--|:--|:--|:--|
|open_price|float64|Yahoo Finance|The open stock price for the given trade day|
|tweet_word_count_sum|int64|Twitter|The total number of word counts of all tweets mentioning about gun control for the given date|
|tweet_compound_score_sum|float64|Twitter|The total compound score (sentiment) of all tweets mentioning about gun control for the given date|
|tweets_sum|int64|Twitter|The total counts of all tweets mentioning about gun control for the given date|
|tweet_word_count_mean|float64|Twitter|The mean of word counts of all tweets mentioning about gun control for the given date|
|tweet_compound_score_mean|float64|Twitter|The compound score mean of all tweets mentioning about gun control for the given date|
|redd_gun_score_mean|float64|/guns subreddit|The subreddit score mean of all the threads on /guns for the given date|
|redd_gun_comment_mean|float64|/guns subreddit|The comment number mean of all the threads on /guns for the given date|
|redd_gun_compound_mean|float64|/guns subreddit|The compound score mean of all the threads on /guns for the given date|
|redd_gun_score_sum|float64|/guns subreddit|The subreddit score sum of all the threads on /guns for the given date|
|redd_gun_comment_sum|float64|/guns subreddit|The total number of comment counts of all the threads on /guns for the given date|
|redd_gun_post_count|float64|/guns subreddit|The total number of thread counts of all the threads on /guns for the given date|
|redd_pol_score_mean|float64|/politics subreddit|The subreddit score mean of all the threads on /politics for the given date|
|redd_pol_comment_mean|float64|/politics subreddit|The comment number mean of all the threads on /politics for the given date|
|redd_pol_compound_mean|float64|/politics subreddit|The compound score mean of all the threads on /politics for the given date|
|redd_pol_score_sum|float64|/politics subreddit|The subreddit score sum of all the threads on /politics for the given date|
|redd_pol_comment_sum|float64|/politics subreddit|The total number of comment counts of all the threads on /politics for the given date|
|redd_pol_post_count|float64|/politics subreddit|The total number of thread counts of all the threads on /politics for the given date|
|10-k|float64|SEC|The RGR 10-K public reports from SEC|
|10-q|float64|SEC|The RGR 10-Q public reports from SEC|
|8-k|float64|SEC|The RGR 8-K public reports from SEC|

## Jupyter Notebooks

This project consists of 7 Jupyter notebooks:
- [Part-1-stock-price-data](./code/Part-1-stock-price-data.ipynb)
- [Part-2-twitter-scraper](./code/Part-2-twitter-scraper.ipynb)
- [Part-3-twitter-data-cleaning](./code/Part-3-twitter-data-cleaning.ipynb)
- [Part-4-reddit-data-scraper](./code/Part-4-reddit-data-scraper.ipynb)
- [Part-5-reddit-data-cleaning](./code/Part-5-reddit-data-cleaning.ipynb)
- [Part-6-sec-data-cleaning](./code/Part-6-sec-data-cleaning.ipynb)
- [Part-7-modeling-and-evaluation](./code/Part-7-modeling-and-evaluation.ipynb)

## Conclusion

The best SARIMAX model with the best AIC score is (0, 1, 1) X (0, 0, 1, 6). It is more intuitive to use 5 as our seasonal component because there are 5 trading days in a week, however, S = 6 has a better AIC score so we ended up using it as our final model. The predictions of our final SARIMAX model are off, this is disappointed because I have included so many X variables to help the model. Instead of predicting the stock open price, I have tried to predict the stock open price percentage change using SARIMAX model as well. The model performed as bad as predicting the open price directly.

Besides SARIMAX models, I have used neural networks to predict the stock price. And the result did not go well. As a consequence, I decided to change my original goal; now I just want to predict if the stock price would go up or go down the next trade day based on public opinion on gun control. The good news is that the classification model I built using neural network actually performed better than other ones. So I implemented this model to a Flask app.

## Final Product

The demonstration video can be found [here](https://www.youtube.com/watch?v=sHMiREufyI4&feature=youtu.be). Although the accuracy score is only around 62%, it is still better than the baseline score (50% by guessing randomly). The information that the stock price will go up or down is somehow not very useful because we don't know the magnitude.

## Improvement

1. More data may help. I built the model on data from 2016 October - 2019 October because scraping Twitter data took a lot of time. So I would like to see how much the models will improve if we have more data.
2. More useful exogenous variables. I have included 20 features already, but some of them are not helping the model. It seems like the financial reports 10Q, 10k, and 8K don't help much.
3. Better models. I did not dig into the popular neural network models due to time limitation. I will definitely check out [LSTM](https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/) and some other models.


## Reference

- [Yahoo Finance](https://finance.yahoo.com/quote/RGR/history?p=RGR)
- [SEC](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000095029&type=&dateb=&owner=exclude&count=100)
- [twitter](https://twitter.com/)
- [twitterscraper](https://github.com/taspinar/twitterscraper)
- [A Guide to Time Series Forecasting with ARIMA in Python 3](https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3)
- [How to Scrap Reddit using pushshift.io via Python](https://medium.com/@pasdan/how-to-scrap-reddit-using-pushshift-io-via-python-a3ebcc9b83f4)
- [List of mass shootings in the United States](https://en.wikipedia.org/wiki/List_of_mass_shootings_in_the_United_States)
- [Bug in ARIMA predict(): ValueError: Must provide freq argument if no data is supplied #3534](https://github.com/statsmodels/statsmodels/issues/3534)
- [Using AIC to Test ARIMA Models](https://coolstatsblog.com/2013/08/14/using-aic-to-test-arima-models-2/)