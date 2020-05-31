import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '$$')

@client.event
async def on_ready():
	print("XtremeBot is ready.")

@client.command()
async def ping(ctx):
	await ctx.send("Pong!")

client.run(os.getenv('Token'))
