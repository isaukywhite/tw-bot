import requests
import random

def daily_message() -> str | None:
    random_number = random.randint(1, 4)
    if random_number == 1:
        return None
    elif random_number == 2:
        return kenye_quote()
    elif random_number == 3:
        return chuck_norris()
    elif random_number == 4:
        return advices_sleep()

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

def advices_sleep():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    advice = response.json()['slip']['advice']
    return advice