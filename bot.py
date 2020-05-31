import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print("XtremeBot is ready.")

@client.event
async def on_message(message):
    if message.content.find("$ping") != -1:
        await message.channel.send('Pong! ' + client.latency() + "ms")

@client.event
async def on_message(message):
    if message.content.find("$hello") != -1:
        await message.channel.send("Hi") # If the user says !hello we will send back hi

client.run(os.getenv('Token'))
