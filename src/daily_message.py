import requests
import random

def daily_message() -> str | None:
    random_number = random.randint(1, 3)
    if random_number == 1:
        return kenye_quote()
    elif random_number == 2:
        return chuck_norris()
    else:
        return None

def kenye_quote():
    url = "https://api.kanye.rest"
    response = requests.get(url)
    advice = response.json()['quote']
    return advice

def chuck_norris():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    advice = response.json()['value']
    return advice