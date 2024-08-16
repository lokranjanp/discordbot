import requests
import random
from discord import *
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands.cooldowns import BucketType
import os
import json

async def deal_user_message(message):
    if message.content.startswith("$insult"):
        random_insult = getInsult()
        await message.channel.send(random_insult)

    if message.content.startswith("$joke"):
        random_joke = getJoke()
        await message.channel.send(random_joke)

    if message.content.startswith("$comp"):
        random_comp = getCompliment()
        await message.channel.send(random_comp)

    if message.content.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)


def getInsult():
    switcher = random.randint(1, 10)
    if switcher%2:
        response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        return response.json()['insult']
    else:
        return random.choice(open('content/insults.txt').read().splitlines())


def getCompliment():
    switcher = random.randint(1, 10)
    if switcher % 2:
        response = requests.get("https://complimentr.com/api")
        return response.json()['compliment']
    else:
        return random.choice(open('content/compliments.txt').read().splitlines())


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    quote_data = json.loads(response.text)
    quote = quote_data[0]['q']+" - "+quote_data[0]['a']
    return quote


def getJoke():
    switcher = random.randint(1, 11)
    if switcher % 2:
        response = requests.get("https://v2.jokeapi.dev/joke/Programming,Dark,Pun")
        if (response.json()['type'] == "twopart"):
            return [response.json()['setup'], response.json()['delivery']]
        else:
            return response.json()['joke']
    else:
        return random.choice(open('content/jokes.txt').read().splitlines())

print(getJoke())