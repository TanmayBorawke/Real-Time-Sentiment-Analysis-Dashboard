import pandas as pd
import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt

# Title
st.title("📊 Real-Time Sentiment Analysis Dashboard")

# Load Dataset
df = pd.read_csv("tweets_sample.csv")

# Function to get sentiment
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["text"].apply(get_sentiment)

# Display Data
st.subheader("Dataset with Sentiment Tags")
st.dataframe(df)

# Count sentiments
sentiment_counts = df["Sentiment"].value_counts()

# Bar chart
st.subheader("Sentiment Distribution")
fig, ax = plt.subplots()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'], ax=ax)
st.pyplot(fig)

# Pie chart
st.subheader("Sentiment Pie Chart")
fig2, ax2 = plt.subplots()
sentiment_counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'red', 'gray'], ax=ax2)
st.pyplot(fig2)
