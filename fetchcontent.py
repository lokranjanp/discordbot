import requests
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
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    return response.json()['insult']


def getCompliment():
    response = requests.get("https://complimentr.com/api")
    return response.json()['compliment']


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    quote_data = json.loads(response.text)
    quote = quote_data[0]['q']+" - "+quote_data[0]['a']
    return quote


#
def getJoke():
    response = requests.get("https://sv443.net/jokeapi/v2/joke/Any")
    if (response.json()['type'] == "twopart"):
        print([response.json()['setup'], response.json()['delivery']])
        return [response.json()['setup'], response.json()['delivery']]
    else:
        return response.json()['joke']
