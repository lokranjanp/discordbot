from discord import *
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands.cooldowns import BucketType
import os
from dotenv import *
from fetchcontent import *

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD")
intents = Intents.all()
client = Client(intents=intents)

@client.event()
async def on_ready():
    print("Logged in as, "+ client.user +". Have fun my boy!")

@client.event()
async def member_joins(member):
    response = "Welcome and get onboard, <@"+str(member.id)+">, "+getInsult()
    for channel in member.guild.channels:
        if channel.name == 'general':
            await channel.send(response)


@client.event()
@commands.cooldown(1, 30, commands.BucketType.user)
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$"):
        deal_user_message(message)

