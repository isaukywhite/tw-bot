from googletrans import Translator
import requests
import random
import json

def translate_text(text: str, target_language: str = "pt") -> str:
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def daily_message() -> str | None:
    random_number = random.randint(1, 2)
    if random_number == 1:
        return None
    elif random_number == 2:
        return from_json()
    
def from_json():
    with open("src/daily_message.json") as file:
        data = json.load(file)
        list_messages = data["conselhos"]
        random_index = random.randint(0, len(list_messages) - 1)
        return list_messages[random_index]
        

def kenye_quote():
    url = "https://api.kanye.rest"
    response = requests.get(url)
    advice = response.json()['quote']
    return translate_text(advice)

def chuck_norris():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    advice = response.json()['value']
    return translate_text(advice)

def advices_sleep():
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    advice = response.json()['slip']['advice']
    return translate_text(advice)

if __name__ == "__main__":
    message = from_json()
    print(message)