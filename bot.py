import discord
import os
from discord.ext import commands
 
client = commands.Bot(command_prefix = '$')

def isprime(num):
	if type(num) != type(1):
		try:
			num = int(num)
		except ValueError:
			return "Incorrect input"
	if num > 1:
	   for i in range(2,num):
	       if (num % i) == 0:
	           return str(num) + " is not a prime number"
	           return str(i) + " times " str(num//i) + " is " + str(num)
	           break
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
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.find("$b") != -1:
        await message.channel.send("🅱️🐝")
 
    if message.content.find("$ping") != -1:
        await message.channel.send("Pong! " + str(client.latency()) + "ms") # Doesn't work'
 
    if message.content.startswith("$test"):
        await message.channel.send(isprime(str(str(message.content) + " ")[6:-1]))
 
    if message.content.startswith("$info"):
        await message.channel.send("I am XtremeBot. A discord bot made by @TheXtremeCrafter#7969. (Intentional no ping)")
 
client.run(os.getenv('Token'))
 