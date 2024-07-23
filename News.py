import requests

def get_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "INDIA",  # Change this to your country code if needed
        "apiKey": "eb3ca6a55a03493cbc167da8fab137bf"  # Replace with your NewsAPI key
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles = data.get("articles", [])
    headlines = [article["title"] for article in articles]
    return headlines
