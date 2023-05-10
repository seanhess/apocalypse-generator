# bot.py
import os
import discord
import random
import rules
from discord.ui import Button
from rules import Move
from discord import app_commands, SelectOption, Interaction
# from discord.ext import commands
# from discord.app_commands import Choice
from typing import Any, Literal, Optional

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


class SimpleView(discord.ui.View):

  foo : Optional[bool] = None
  message: Optional[discord.Message]

  async def disable_all_items(self):
    for item in self.children:
      print("DISAVLING")
      item.disabled = True

    # This is how you update the message!
    # await self.message.edit(view=self)

  async def on_timeout(self) -> None:
    await self.disable_all_items()
    if self.message:
      await self.message.channel.send("Timeout")
    else:
      print("NO MESSAGE!")

  @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
  async def hello(self, interaction:Interaction, button: discord.ui.Button):
    # This sends another message
    print("- CLICK HELLO")
    await interaction.response.send_message("World")
    print("- AFTER HELLO")

  @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
  async def cancel(self, interaction:Interaction, button: discord.ui.Button):
    print("- CLICK CANCEL")
    await self.disable_all_items()
    await interaction.response.edit_message(view=self)


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


@tree.command(name = 'view', description = 'Test view', guild=discord.Object(id=ENIGMA_GUILD))
async def view(ctx:Interaction):
  view = SimpleView(timeout=180)
  # button:Button = discord.ui.Button(label="Click me")
  # view.add_item(button)
  view.message = ctx.message

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


# client.run(TOKEN)
# bot.run(TOKEN)
TOKEN=os.getenv("DISCORD_TOKEN")
client.run(TOKEN if TOKEN else "")



