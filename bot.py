# bot.py
import os
import discord
import random

from lib.dungeon_world import Character, Name
import lib.component
from lib.storage import character_find
from lib.character import CharacterView
from discord.emoji import Emoji
from discord.enums import ButtonStyle
from discord.partial_emoji import PartialEmoji
import rules
from discord.ui import Button
from rules import Move
from discord import app_commands, SelectOption, Interaction
# from discord.ext import commands
# from discord.app_commands import Choice
from typing import Any, Literal, Optional, Union, List, Dict

ENIGMA_GUILD=1105180075558707293

intents = discord.Intents().default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='$', intents=intents)

tree:Any = app_commands.CommandTree(client)

characters:Dict[Name, Character] = {}

def main():
  print("Apocalypse Bot!")
  print("===============")
  TOKEN=os.getenv("DISCORD_TOKEN")
  client.run(TOKEN if TOKEN else "")


@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=ENIGMA_GUILD))
  print(" |0_0| Meep Moop")




Faction = Literal['Mortalis', 'Night', 'Power', 'Wild']

# @Bot.command()
# async def ping(ctx, arg):
#     await ctx.channel.send("pong")

@tree.command(name = 'move', description = 'Choose an MC Move', guild=discord.Object(id=ENIGMA_GUILD))
async def move(ctx:Interaction, faction:Optional[Faction]):

  moves = mc_moves(faction)
  rand_moves = random.sample(moves, 3)
  names = map(lambda m: "move: " + m.name, rand_moves)
  output = "\n".join(names)
  await ctx.response.send_message(output)


@tree.command(name = 'character', description = 'Create or select a character', guild=discord.Object(id=ENIGMA_GUILD))
async def character(ctx:Interaction, name:str):
  char = character_find(characters, name)
  view = CharacterView(timeout=10)
  view.set_character(char)
  await ctx.response.send_message(char.name, view=view)
  # await ctx.response.send_message("HI:" + char.name)


@tree.command(name = 'roll', description = 'roll some dice', guild=discord.Object(id=ENIGMA_GUILD))
async def roll(ctx:Interaction, dice:str):

  total = 0
  lstDice = []
  [count, sides] = dice.split("d")
  countI = int(count)
  sidesI = int(sides)
  for num in range(countI):
    die = random.randint(1, sidesI)
    lstDice.append("die #"+str(num+1)+': ' + str(die))
    total = total + die
  dieStr = "total: " + str(total) + "\n"
  for lstDie in lstDice:
    dieStr += lstDie + "\n"
  await ctx.response.send_message(dieStr)
    

@tree.command(name = 'view', description = 'Test view', guild=discord.Object(id=ENIGMA_GUILD))
async def view(ctx:Interaction):
  view = McMoveView(timeout=180)
  # button:Button = discord.ui.Button(label="Click me")
  # view.add_item(button)
  view.add_buttons(rules.moves)
  # view.message = ctx.message
  # view.moves = rules.moves

  await ctx.response.send_message(view=view)
  print("- done")

  # # This waits for the view to finish. Either Timeout, or one of the buttons are pressed
  # # No, it fails
  # await view.wait()

  # if (view.foo is None):
  #   print("Timeout")
  # elif view.foo is True:
  #   print("Ok")
  # else:
  #   print("Cancel")



# @bot.command()
# async def hello(ctx, *, arg):
#     await ctx.send("hello: " + arg)


def mc_moves(faction:Optional[Faction]) -> list[Move]:
  return rules.moves
  # basic = [
  #   "Surface a conflict, ancient or modern",
  #   "Put someone in danger",
  #   "Inflict (or trade) harm",
  #   "Propose an opportunity with a cost"
  # ]

  # mortalis = [
  #   "Adapt to the changing circumstances",
  #   "Gather in numbers to confront a threat"
  # ]

  # night = [
  #   "Display an aggressive show of force",
  #   "Threaten someone's interests or holdings"
  # ]

  # power = [
  #   "Impose a cost for the greater good",
  #   "Mystically foreshadow a conflict or challenge"
  # ]

  # wild = [
  #   "Challeng the PCs with alien expectations and traditions",
  #   "Offer extraordinary assistance for a sticky price"
  # ]

  # match faction:
  #   case "Mortalis": return basic + mortalis
  #   case "Night": return basic + night
  #   case "Power": return basic + power
  #   case "Wild": return basic + wild
  #   case _: return basic


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

class McMoveView(discord.ui.View):

  moves: list[Move]

  def add_buttons(self, moves:list[Move]):
    self.moves = moves
    for move in moves:
      button = lib.component.DynButton(label=move.name, style=discord.ButtonStyle.green)
      button.set_callback(self.callback)
      self.add_item(button)

  async def callback(self, interaction:Interaction):
    print("CALLED!", self)

    children:List[lib.component.DynButton] = self.children # type: ignore
    
    # Disable all buttons
    for item in children:
        item.disabled = True

    # Update the message
    await interaction.response.edit_message(content="Buttons are now disabled", view=self)

  async def on_timeout(self) -> None:
    # await self.disable_all_items()
    # if self.message:
    #   await self.message.channel.send("Timeout")
    # else:
    print("Timeout!")

  # @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
  # async def hello(self, interaction:Interaction, button: discord.ui.Button):
  #   # This sends another message
  #   print("- CLICK HELLO")
  #   await interaction.response.send_message("World")
  #   print("- AFTER HELLO")

  # @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
  # async def cancel(self, interaction:Interaction, button: discord.ui.Button):
  #   print("- CLICK CANCEL")
  #   await self.disable_all_items()
  #   await interaction.response.edit_message(view=self)





main()