import discord
import os
from discord.ext import commands

prefix = "$"

client = commands.Bot(command_prefix = prefix)

def isprime(num):
    if type(num) != type(1):
        try:
            num = int(num)
        except ValueError:
            return "Invalid input value."
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return str(num) + " is not a prime number" + "\n" + str(i) + " times " +  str(num//i) + " is " + str(num)

        else:
            return str(num) + " is a prime number"

    else:
        return str(num) + " is not a prime number"

@client.event
async def on_ready():
    print("XtremeBot is ready.")
 
#@client.command()
#async def ping(ctx):
    #await ctx.send('Pong!')

@client.command()
async def pinga(ctx):
    await ctx.send('Pong! {}'.format(round(client.latency, 1)))

@client.command()
async def pingb(ctx):
    await ctx.send(f'My ping is {client.latency}!')

@client.command()
async def pingc(ctx):
    await ctx.send(f'My ping is {bot.latency}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.find(prefix+"b") != -1:
        await message.channel.send("🅱️🐝")

    #if message.content.find(prefix+"ping") != -1:
        #await message.channel.send("Pong! " + str(round(client.latency())) + "ms") # Doesn't work'

    if message.content.startswith(prefix+"prime"):
        try:
            await message.channel.send(isprime(str(str(message.content) + " ")[6:-1]))
        except IndexError:
            return

    if message.content.startswith(prefix+"eval"):
        try:
            await message.channel.send(eval(str(str(message.content)+" ")[5:-1]))
        except:
            await message.channel.send("Invalid input")

    if message.content.startswith(prefix+"say"):
        await message.channel.send(str(str(message.content)+" ")[4:-1])

    if message.content.startswith(prefix+"help"):
        await message.channel.send("Commands list:\n`b` : Just B.\n`prime` : Check if a number is prime or not.\n`eval` : Evaluate your [mathematical] statement. This accepts Python syntax.\n`say` : Says whatever you say after the command.\n`info` : Information about the bot.")

    if message.content.startswith(prefix+"info"):
        await message.channel.send("I am XtremeBot. A discord bot made by @TheXtremeCrafter#7969. (Intentional no ping)\nDiscord.py version info:")
        await message.channel.send(str(discord.version_info) + "\n" + str(discord.__version__))

    await client.process_commands(message)

client.run(os.getenv('Token'))
