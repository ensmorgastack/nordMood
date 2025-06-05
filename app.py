import streamlit as st
from textblob import TextBlob
from deep_translator import GoogleTranslator

language_codes = {
    "🇧🇬 Bulgarian": "bg",
    "🇨🇳 Chinese (Simplified)": "zh-CN",
    "🇨🇿 Czech": "cs",
    "🇩🇰 Danish": "da",
    "🇳🇱 Dutch": "nl",
    "🇬🇧 English": "en",
    "🇪🇪 Estonian": "et",
    "🇫🇮 Finnish": "fi",
    "🇫🇷 French": "fr",
    "🇩🇪 German": "de",
    "🇬🇷 Greek": "el",
    "🇭🇺 Hungarian": "hu",
    "🇮🇩 Indonesian": "id",
    "🇮🇹 Italian": "it",
    "🇯🇵 Japanese": "ja",
    "🇰🇷 Korean": "ko",
    "🇱🇻 Latvian": "lv",
    "🇱🇹 Lithuanian": "lt",
    "🇳🇴 Norwegian (Bokmål)": "no",
    "🇵🇱 Polish": "pl",
    "🇵🇹 Portuguese": "pt",
    "🇷🇴 Romanian": "ro",
    "🇷🇺 Russian": "ru",
    "🇸🇰 Slovak": "sk",
    "🇸🇮 Slovenian": "sl",
    "🇪🇸 Spanish": "es",
    "🇸🇪 Swedish": "sv",
    "🇹🇷 Turkish": "tr",
    "🇺🇦 Ukrainian": "uk"
}


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "Positive 😊"
    elif polarity < -0.2:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def translate(text, from_lang, to_lang):
    return GoogleTranslator(source = from_lang, target = to_lang).translate(text)

st.title("DEV NordMood: Sentiment Translator to Swedish")

option = st.selectbox(
    "Pick language",
    (language_codes),
)

user_input = st.text_input(f"Enter a sentence in {option[2:]}")

if user_input:
    from_language = language_codes.get(option)
    phrase = user_input
    if from_language != "en":
        phrase = translate(user_input, from_language, 'en')

    sentiment = analyze_sentiment(phrase)
    translation = translate(user_input, language_codes.get(option), 'sv')
    
    st.markdown(f"*Sentiment:* {sentiment}")
    st.markdown(f"*Swedish Translation:* {translation}")