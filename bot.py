import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print("XtremeBot is ready.")

#@client.command()
#async def ping(ctx):
	#await ctx.send('Pong!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.find("$b") != -1:
        await message.channel.send("🅱️🐝")

    if message.content.find("$ping") != -1:
        await message.channel.send("Pong! " + str(client.latency()) + "ms")

    if message.content.startswith("$test"):
        await message.channel.send("test true")

    if message.content.startswith("$info"):
        await message.channel.send("I am XtremeBot. A discord bot made by @TheXtremeCrafter#7969")

client.run(os.getenv('Token'))
