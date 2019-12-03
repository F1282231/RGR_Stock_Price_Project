# RGR Stock Price Forecasting Project

Author: [Jack Wang](https://www.linkedin.com/in/jackweijiawang/)

---

## Problem Statement

Stock prices are hard to predict because they are not only affected by the performance of the underlying companies but also the expectations from the general public. As known, the stock price of firearm companies are highly correlated to the public opinions toward gun control. My model intends to predict the stock price of one of the largest firearm company in the states, RGR (Sturm, Ruger & Co., firearm company), by using its historical stock price, public opinions toward gun control, and its financial reports to SEC. 

---

## Executive Summary

The goal of my projcet is to build a **time series regression model** that predicts the stock price of RGR. The data I am using would be historical stock price from [Yahoo Finance](https://finance.yahoo.com/quote/RGR/history?p=RGR), twitter posts scraped from [twitter](https://twitter.com/), subreddit posts mentioned about gun control, and also the financial reports to [SEC](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000095029&type=&dateb=&owner=exclude&count=100). I will do sentiment analysis on the text data and time series modeling on the historical stock price data. The model will be evaluated using MSE.

---

## Software Requirements

Codes are written in Jupyter Notebook with Python. Users are recommended to know Python library `Numpy`, `Pandas`, time series models with `statsmodels.tsa` and `keras`, visualization with `matplotlib`, and the knowledge of ARIMA, SARIMAX, and neural networks.

---

## Content

This project consists of 7 Jupyter notebooks:
- [Part-1-stock-price-data](./code/Part-1-stock-price-data.ipynb)
- [Part-2-twitter-scraper](./code/Part-2-twitter-scraper.ipynb)
- [Part-3-twitter-data-cleaning](./code/Part-3-twitter-data-cleaning.ipynb)
- [Part-4-reddit-data-scraper](./code/Part-4-reddit-data-scraper.ipynb)
- [Part-5-reddit-data-cleaning](./code/Part-5-reddit-data-cleaning.ipynb)
- [Part-6-sec-data-cleaning](./code/Part-6-sec-data-cleaning.ipynb)
- [Part-7-modeling-and-evaluation](./code/Part-7-modeling-and-evaluation.ipynb)

---

## Conclusion



## Reference

- [Yahoo Finance](https://finance.yahoo.com/quote/RGR/history?p=RGR)
- [SEC](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000095029&type=&dateb=&owner=exclude&count=100)
- [twitter](https://twitter.com/)
- [twitterscraper](https://github.com/taspinar/twitterscraper)
- [A Guide to Time Series Forecasting with ARIMA in Python 3](https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3)
- [How to Scrap Reddit using pushshift.io via Python](https://medium.com/@pasdan/how-to-scrap-reddit-using-pushshift-io-via-python-a3ebcc9b83f4)
- [List of mass shootings in the United States](https://en.wikipedia.org/wiki/List_of_mass_shootings_in_the_United_States)
