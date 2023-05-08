# bot.py
import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

class MissingAPIKey(Exception):
  """Raised when API Key environment variable is missing"""

if TOKEN is None:
  raise MissingAPIKey()

print("TOKEN", TOKEN)


ENIGMA_GUILD=1105180075558707293


intents = discord.Intents().default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='$', intents=intents)

tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=ENIGMA_GUILD))
  print("Apocalypse Bot is revved up and ready to go!")



# @Bot.command()
# async def ping(ctx, arg):
#     await ctx.channel.send("pong")

@tree.command(name = 'ping', description = 'testing slash commands!', guild=discord.Object(id=ENIGMA_GUILD))
async def ping(ctx):
    await ctx.response.send_message("pong")
    # await interaction.response.send_message("hello")

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
client.run(TOKEN)



