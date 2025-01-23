import requests

def daily_message():
    url = "https://api.kanye.rest"
    response = requests.get(url)
    advice = response.json()['quote']
    return advice