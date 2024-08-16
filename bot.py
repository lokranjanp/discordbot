import random
import time, datetime
from discord import Intents, Client, Message
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands.cooldowns import BucketType
import os
from typing import Final
from dotenv import *
from fetchcontent import *

load_dotenv()

DISCORD_TOKEN: Final[str] = os.getenv("DISCORD")
intents = Intents.all()
client = Client(command_prefix="$", intents=intents)
restricted_users = {}
seed = int(time.time()*1000)%1000
random.seed(seed)

@client.event
async def on_ready():
    print("Logged in as, "+ str(client.user) +". Have fun!")

@client.event
async def member_joins(member):
    response = "Welcome and get onboard, <@"+str(member.id)+">, "+getInsult()
    for channel in member.guild.channels:
        if channel.name == 'general':
            await channel.send(response)


# @client.event
def deal_user_message(message):
    if message.content.startswith("$insult"):
        random_insult = getInsult()
        return message.channel.send(random_insult)

    if message.content.startswith("$joke"):
        random_joke = getJoke()
        return message.channel.send(random_joke)

    if message.content.startswith("$compliment"):
        random_comp = getCompliment()
        return message.channel.send(random_comp)

    if message.content.startswith("$inspire"):
        quote = get_quote()
        return message.channel.send(quote)


def reaction():
    return random.choice(["🍆", "🗿", "😮‍💨", "❌", "🤓", "🥸", "🤡"])


@client.event
async def start_game(user):
    if user=="Cooper":
        await "I dont mess with an Odinson. 🗿"
    initmessage = "Alright mf lets do this... "+str(user.mention)+" ."
    await initmessage
    await getInsult()


@client.event
@commands.cooldown(10, 30, commands.BucketType.user)
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$roulette"):
        start_game(message.author)

    if message.content.startswith("$"):
        await deal_user_message(message)
        await message.add_reaction(reaction())


client.run(DISCORD_TOKEN)

