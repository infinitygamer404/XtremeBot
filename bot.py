import discord
import os
import mf
from discord.ext import commands

prefix = "./"

client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print("XtremeBot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ` {round(client.latency * 1000, 3)} `ms ')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.find(prefix+"b") != -1:
        await message.channel.send("🅱️🐝")

    if message.content.startswith(prefix+"prime"):
        await message.channel.send(mf.isprime(str(str(message.content) + " ")[len(prefix)+len("prime"):-1]))

    if message.content.startswith(prefix+"fib"):
        await message.channel.send(str(mf.fib(str(str(message.content) + " ")[len(prefix)+len("fib"):-1])))

    if message.content.startswith(prefix+"eval"):
        try:
            await message.channel.send(eval(str(str(message.content)+" ")[len(prefix)+len("eval"):-1]))
        except:
            await message.channel.send("Invalid input")

    if message.content.startswith(prefix+"say"):
        await message.channel.send(str(str(message.content)+" ")[len(prefix)+len("say"):-1])

    if message.content.startswith(prefix+"help"):
        await message.channel.send("Commands list:\n`b` : Just B.\n`prime` : Check if a number is prime or not.\n`eval` : Evaluate your [mathematical] statement. This accepts Python syntax.\n`say` : Says whatever you say after the command.\n`ping` : Pong!\n`info` : Information about the bot.")

    if message.content.startswith(prefix+"info"):
        await message.channel.send("I am XtremeBot. A discord bot made by @TheXtremeCrafter#7969. (Intentional no ping)\nDiscord.py version info:")
        await message.channel.send(str(discord.version_info) + "\n" + str(discord.__version__))

    await client.process_commands(message)

client.run(os.getenv('Token'))
