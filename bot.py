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
client = Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in as, "+ client.user +". Have fun!")

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

    if message.content.startswith("$comp"):
        random_comp = getCompliment()
        return message.channel.send(random_comp)

    if message.content.startswith("$inspire"):
        quote = get_quote()
        return message.channel.send(quote)


@client.event
@commands.cooldown(10, 30, commands.BucketType.user)
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$"):
        await deal_user_message(message)

client.run(DISCORD_TOKEN)

