import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print("XtremeBot is ready.")

@client.command()
async def ping(ctx):
	await ctx.send('Pong!')

@client.event
async def on_message(message):
    if message.content.find("$b") != -1:
        await message.channel.send("🅱️🐝")
    if message.content.find("$ping") != -1:
        await message.channel.send("Pong! " + str(client.latency()) + "ms")
    if message.content.startswith("$test"):
        await message.channel.send("test true")
    if not message.content.startswith("$test"):
        await message.channel.send("test false")

client.run(os.getenv('Token'))
