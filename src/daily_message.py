import requests

def daily_message():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    advice = response.json()['slip']['advice']
    return advice