# imports
import pandas as pd
import numpy as np
import pickle
import time, datetime
import re
import pickle
from sklearn.externals import joblib
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.keras.models import load_model
from datetime import timedelta
from twitterscraper import query_tweets
from flask import Flask, request, Response, render_template, jsonify
from twitterscraper import query_tweets
from nltk.tokenize import RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# initialize the flask app
app = Flask('myApp')

@app.route('/form')
def form():
    time_now = datetime.datetime.today().date()
    return render_template('form.html', time=time_now)

# define the route
@app.route('/submit')
def submit():

    #scraper function
    def scrape_twitter():
        # set empty lists that we will fill with tweet data
        # Keywords I want to search for
        query_string = f'"gun ban" OR "gun control" OR "firearm control" OR'\
                       f' "gun-control" OR "firearm-control" OR "gun reform" OR "gun-reform" OR'\
                       f' "firearm-reform" OR "firearm reform" -filter:retweets'
        # set empty lists that we will fill with tweet data
        text = []
        times = []

        # scrape twitter for tweets containing certain keywords
        list_of_tweets = query_tweets(query_string,
                                begindate = datetime.datetime.today().date() - timedelta(days=2),
                                enddate = datetime.datetime.today().date() + timedelta(days=1),
                                poolsize = 2,
                                lang="en"
                               )
        # loop through each tweet to grab data and append the data to their respective lists
        for tweet in list_of_tweets:
            text.append(tweet.text)
            times.append(tweet.timestamp)
        # build the dataframe
        df = pd.DataFrame({
            'tweet': text,
            'time_stamp': times
        })
        df = df.drop_duplicates()
        # remove any twitter pic urls
        df['tweet'] = [re.sub(r'pic.twitter.com\S+', '', post).strip() for post in df['tweet']]
        # remove any http urls
        df['tweet'] = [re.sub(r'http\S+', '', post).strip() for post in df['tweet']]
        # instatiate the tokenizer
        tknr = RegexpTokenizer(r'[a-zA-Z&0-9]+')
        # start with empty lists
        tokens = []
        # fill the list with tokenized versions of each post title
        for post in df['tweet']:
            tokens.append(" ".join(tknr.tokenize(post.lower())))
        df['tweet'] = tokens
        # add a word count column
        df['tweet_word_count'] = df['tweet'].apply(lambda post: len(post.split()))
        # compound score added
        sia = SentimentIntensityAnalyzer()
        # create function to return compound score
        def get_compound(text):
            return sia.polarity_scores(text)['compound']
        # add compound score features for title and tac column
        df['compound'] = df['tweet'].map(lambda x : get_compound(x))
        df = df.sort_values(by = 'time_stamp')

        df['time_stamp'] = pd.to_datetime(df['time_stamp']).dt.date

        df = df.drop_duplicates()

        df = df.reset_index(drop=True)

        df = pd.merge(df.groupby(by = 'time_stamp').sum(),pd.merge(df.groupby(by = 'time_stamp').count(), df.groupby(by = 'time_stamp').mean(), left_index= True, right_index = True), left_index= True, right_index = True)

        df = df.drop(columns=['tweet_word_count_x', 'compound_x'])

        df.columns=['tweet_word_count_sum', 'tweet_compound_score_sum', 'tweets_sum', 'tweet_word_count_mean', 'tweet_compound_score_mean']

        return df

    data = scrape_twitter()
    scaler = joblib.load("../assets/scaler.save")
    data_sc = scaler.transform(data)
    test_sequences = TimeseriesGenerator(data_sc, [0,0,0], length = 2, batch_size = 128)

    model = load_model('../assets/final_model.h5')
    prediction = round(model.predict_proba(test_sequences[0][0])[0][0]*100,2)

    time_now = datetime.datetime.today().date()

    return render_template('results.html', time=time_now, prediction= prediction)

# run the app
if __name__ == '__main__':
    app.run(debug=True)
