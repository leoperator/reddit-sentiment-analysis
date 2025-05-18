import streamlit as st
import praw
import pandas as pd
from urllib.parse import urlparse
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
user_agent = os.getenv("REDDIT_USER_AGENT")


nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def analyze_subreddit(subreddit_name):
    posts = []
    for submission in reddit.subreddit(subreddit_name).hot(limit=300):
        if not submission.stickied:
            text = submission.title + " " + submission.selftext
            sentiment = get_sentiment(text)
            posts.append({'Title': submission.title, 'Sentiment': sentiment})
            if len(posts) >= 200:
                break
    return pd.DataFrame(posts)

def analyze_post(url):
    try:
        post_id = urlparse(url).path.split('/')[4]
        submission = reddit.submission(id=post_id)
        comments = []
        submission.comments.replace_more(limit=0)
        for top_level_comment in submission.comments[:10]:
            text = top_level_comment.body
            sentiment = get_sentiment(text)
            comments.append({'Comment': text, 'Sentiment': sentiment})
        return pd.DataFrame(comments)
    except Exception as e:
        st.error(f"Error analyzing post: {e}")
        return pd.DataFrame()

st.title("Reddit Sentiment Analyzer")
input_type = st.radio("Analyze by:", ["Subreddit Name", "Reddit Post URL"])
if input_type == "Subreddit Name":
    subreddit_name = st.text_input("Enter subreddit name (e.g. 'technology')")
    if st.button("Analyze Subreddit"):
        with st.spinner("Analyzing posts..."):
            df = analyze_subreddit(subreddit_name.strip())
            st.success("Analysis complete.")
            st.dataframe(df)
            st.bar_chart(df['Sentiment'].value_counts())
else:
    reddit_url = st.text_input("Enter Reddit post URL (e.g. 'https://www.reddit.com/r/technology/comments/xxxxx/')")
    if st.button("Analyze Post Comments"):
        with st.spinner("Analyzing top comments..."):
            df = analyze_post(reddit_url.strip())
            if not df.empty:
                st.success("Analysis complete.")
                st.dataframe(df)
                st.bar_chart(df['Sentiment'].value_counts())
