import requests
import random
import json

def getInsult():
    switcher = random.randint(1, 10)
    if switcher%2:
        response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        return response.json()['insult']
    else:
        return random.choice(open('content/insults.txt').read().splitlines())


def getCompliment():
        return random.choice(open('content/compliments.txt').read().splitlines())


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    quote_data = json.loads(response.text)
    quote = quote_data[0]['q']+" - "+quote_data[0]['a']
    return quote


def getJoke():
    switcher = random.randint(1, 10)
    if switcher % 2:
        response = requests.get("https://v2.jokeapi.dev/joke/Programming,Dark,Pun")
        if (response.json()['type'] == "twopart"):
            return response.json()['setup'], response.json()['delivery']
        else:
            return response.json()['joke']
    else:
        return random.choice(open('content/jokes.txt').read().splitlines())
