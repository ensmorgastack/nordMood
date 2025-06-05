import streamlit as st
from textblob import TextBlob
from deep_translator import GoogleTranslator

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "Positive 😊"
    elif polarity < -0.2:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def translate_to_swedish(text):
    return GoogleTranslator(source='en', target='sv').translate(text)

st.title("DEV NordMood: Emotional Translator to Swedish")

user_input = st.text_input("Enter a sentence in English")

if user_input:
    sentiment = analyze_sentiment(user_input)
    translation = translate_to_swedish(user_input)
    
    st.markdown(f"*Sentiment:* {sentiment}")
    st.markdown(f"*Swedish Translation:* {translation}")