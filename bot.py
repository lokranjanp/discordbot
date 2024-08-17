import time
import asyncio
from discord import Intents, Client, Message
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands.cooldowns import BucketType
from typing import Final
from dotenv import *
import os
from fetchcontent import *

load_dotenv()
resistant_users = set()

DISCORD_TOKEN: Final[str] = os.getenv("DISCORD")
intents = Intents.all()
client = Client(command_prefix="$", intents=intents)
restricted_users = {}
seed = int(time.time()*1000) % 1000
random.seed(seed)

@client.event
async def on_ready():
    print("Logged in as, " + str(client.user) + ". Have fun!")

@client.event
async def member_joins(member):
    response = "Welcome and get onboard, <@"+str(member.id)+">, "+getInsult()
    for channel in member.guild.channels:
        if channel.name == 'general':
            await channel.send(response)


@client.event
async def deal_user_message(message):
    if message.content.startswith("$insult"):
        random_insult = getInsult()
        await message.channel.send(random_insult)

    if message.content.startswith("$joke"):
        random_joke = getJoke()
        await message.channel.send(random_joke)

    if message.content.startswith("$compliment"):
        random_comp = getCompliment()
        await message.channel.send(random_comp)

    if message.content.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)


def reaction():
    return random.choice(["🍆", "🗿", "😮‍💨", "❌", "🤓", "🥸", "🤡", "🍆", "🍆", "🍆", "🍆"])


async def resistant(user):
    """Toggles a user as resistant or not."""
    if user.id in resistant_users:
        resistant_users.remove(user.id)
        await user.send("You're no longer resistant to my tricks! 🤡")
    else:
        resistant_users.add(user.id)
        await user.send("You're now resistant to my tricks. 🗿")


@client.event
async def toggle_resistant(user, member):
    """Command to toggle resistant status for a user."""
    print(member)
    await resistant(member)
    await user.send(f'{member.display_name}\'s resistant status has been toggled!')


@client.event
async def start_game(user):
    print(user)
    if user.id in resistant_users:
        await user.send("I don't mess with the resistant ones. 🗿")
        return
    init_message = f"Alright mf, let's do this... {user.mention}."
    await user.send(init_message)
    for _ in range(10):
        insult = getInsult()
        await user.send(insult)
        await asyncio.sleep(10)


@client.event
@commands.cooldown(10, 20, commands.BucketType.user)
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$resistant"):
        await toggle_resistant(user = message.author, member=message.author)

    if message.content.startswith("$roulette"):
        await start_game(message.author)

    if message.content.startswith("$"):
        await deal_user_message(message)
        await message.add_reaction(reaction())


client.run(DISCORD_TOKEN)
