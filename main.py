#XerBot by Xernot

import discord
import time
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='>>')


@bot.event
async def on_ready():
    print("I am ready")
    print("I am using the ID: " + bot.user.id)

@bot.event
async def on_message_delete(message):
    print("{} deleted a message saying: {} (TIME): {}".format(message.author, message.content, time.ctime))

@bot.event
async def on_message(message):

    channel = message.channel
    server = message.server
    user = message.author
    print("(SERVER): {} (CHANNEL): {} (AUTHOR): {} (CONTENT): {} (TIME): {}".format(server, channel, message.author, message.content, time.ctime()))
    file = open("The_tavvern.txt","a")

    file.write("""{}: {}: {}: {}
""".format(server, channel, user, message.content))
    await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
    print("""EDIT: (((Before))): (SERVER): {}: (CHANNEL): {}: (AUTHOR): {}: (CONTENT): {}
EDIT CONT: (((After))): (SERVER): {}: (CHANNEL): {}: (AUTHOR): {}: (CONTENT): {} (TIME): {}""".format(before.server, before.channel, before.author, before.content, after.server, after.channel, after.author, after.content, time.ctime()))
    file = open("The_tavvern.txt","a")

    file.write("""EDIT: (((Before))): (SERVER): {}: (CHANNEL): {}: (AUTHOR): {}: (CONTENT): {}
EDIT CONT: (((After))): (SERVER): {}: (CHANNEL): {}: (AUTHOR): {}: (CONTENT): {} (TIME): {}
""".format(before.server, before.channel, before.author, before.content, after.server, after.channel, after.author, after.content, time.ctime()))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("<@{}> pinged me!".format(ctx.message.author.id))

@bot.command()
async def echo(*args):
    output = " "
    for word in args:
        output += word
        output += " "
    await bot.say(output)

@bot.command(pass_context=True)
async def info(ctx):
    user = ctx.message.author
    await bot.say("You are: {}".format(user))

@bot.command(pass_context=True)
async def clear(ctx, amount = 10):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages deleted")

bot.run("NDQ2MzgzNTU5NzkyNTI1MzEy.Dh1Orw.iqm1l0EupgWYtRuHJpAeyscvJic")
