# bot.py
import os
import discord

TOKEN = os.getenv('DISCORD_TOKEN')


class MissingAPIKey(Exception):
  """Raised when API Key environment variable is missing"""

if TOKEN is None:
  raise MissingAPIKey()

print("TOKEN", TOKEN)


intents = discord.Intents().default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)



