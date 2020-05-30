import discord

from discord.ext import commands

client = commands.Bot(command_prefix = 'x-')

@client.event

async def on_ready():

	print("XtremeBot is ready.")

@client.command()

async def ping(ctx):

	await ctx.send("Pong!")

client.run('NzE2MjAyMDgzMDYxMzM0MDI2.XtIZIw._fV_MO0uoNDNi9TWFFN6caYtdVU')
