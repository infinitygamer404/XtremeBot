import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'x-')

@client.event
async def on_ready():
	print("XtremeBot is ready.")

@client.command()
async def ping(ctx):
	await ctx.send("Pong!")

client.run(os.getenv('Token'))
