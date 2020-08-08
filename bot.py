import discord
import os
import mf
from discord.ext import commands

PREFIX = "./"

client = commands.Bot(command_prefix = PREFIX)

@client.event
async def on_ready():
    print("XtremeBot is ready.")
    await mf.log()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Didn't find a command with that name, type `./help` for a list of commands. \u274c")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ` {round(client.latency * 1000)} `ms')

@client.command()
async def b(ctx):
    await ctx.send("🅱️🐝")

@client.command(aliases=["isprime"])
async def prime(ctx, num):
    await ctx.send(str(mf.isprime(num)))

@client.command()
async def fib(ctx, num):
    await ctx.send(str(mf.fib(num)))

@client.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

@client.command(aliases=["eval"])
async def _eval(ctx, *, stmt):
    try:
        await ctx.send(str(eval(stmt)))
    except:
        await ctx.send("Invalid input")

@client.command(aliases=["help"])
async def _help(ctx):
    await ctx.send(f"The bot prefix is `{PREFIX}`\nCommands list:\n`{prefix}b` : Just B.\n`{prefix}prime` : Check if a number is prime or not.\n`{prefix}eval` : Evaluate your [mathematical] statement. This accepts Python syntax.\n`{prefix}say` : Says whatever you say after the command.\n`{prefix}ping` : Pong!\n`{prefix}info` : Information about the bot.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix+"info"):
        await message.channel.send("I am XtremeBot. A discord bot made by @TheXtremeCrafter#7969. (Intentional no ping)\nDiscord.py version info:")
        await message.channel.send(str(discord.version_info) + "\n" + str(discord.__version__))

    await client.process_commands(message)

client.run(os.getenv('Token'))
