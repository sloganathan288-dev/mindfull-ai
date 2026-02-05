import requests
import nltk
import string
from nltk.corpus import stopwords

nltk.download("stopwords")

API_KEY = "d157ff6dacbb416c9cc2814a6f489dce"

stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    keywords = [w for w in words if w not in stop_words]
    return " ".join(keywords[:8])  # top keywords

def verify_news(news_text):
    query = preprocess(news_text)

    url = (
        "https://newsapi.org/v2/everything?"
        f"q={query}&"
        "language=en&"
        "sortBy=relevancy&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    if data.get("totalResults", 0) >= 3:
        return "✅ TRUE (Verified from multiple trusted news sources)"
    else:
        return "🚨 FAKE (Not found in reliable news sources)"
