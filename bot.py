# bot.py
import os
import discord
from discord import app_commands, SelectOption, Interaction
from discord.ext import commands
from discord.app_commands import Choice
from typing import Any, Literal

ENIGMA_GUILD=1105180075558707293


intents = discord.Intents().default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='$', intents=intents)

tree:Any = app_commands.CommandTree(client)



@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=ENIGMA_GUILD))
  print("Apocalypse Bot is revved up and ready to go!")



# @Bot.command()
# async def ping(ctx, arg):
#     await ctx.channel.send("pong")

@tree.command(name = 'ping', description = 'testing slash commands!', guild=discord.Object(id=ENIGMA_GUILD))
# @app_commands.choices(choices=[
#     Choice(name="Rock", value="rock"),
#     Choice(name="Paper", value="paper"),
#     Choice(name="Scissors", value="scissors"),
#   ])
# @app_commands.choices()
async def ping(ctx:Interaction, weapon:Literal['apple', 'banana', 'cherry'], asdf:str = "testing"):
    await ctx.response.send_message("pong: " + weapon + " " + asdf)

# @bot.command()
# async def hello(ctx, *, arg):
#     await ctx.send("hello: " + arg)




# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return

#   # if message.content.startswith('$bye'):
#   #   await message.channel.send('bye!')

#   if message.content.startswith('$hello'):
#     await message.channel.send('hi 2')
# # @client.event
# async def on_member_join(member):
#   await member.create_dm()
#   await member.dm_channel.send(
#     "Hi {member.name}, welcome to my discord server"

#   )
#   return


# client.run(TOKEN)
# bot.run(TOKEN)
TOKEN=os.getenv("DISCORD_TOKEN")
client.run(TOKEN if TOKEN else "")



