import discord
import random
from discord import Interaction
from discord.ui import TextInput, View, Modal
from lib.dungeon_world import Character, Stat
from lib.component import DynButton
from typing import Callable, List, Dict, cast
from discord.components import ActionRow

def chaRoll(bonus, name):
  total = 0
  lstDice = []
  bonus = bonus
  
  for num in range(2):
    die = random.randint(1, 6)
    lstDice.append(str(die))
    total = total + die

  if bonus != 0: embed = discord.Embed(title="Rolled " + name +" (+" + bonus + ')', color=discord.Color.dark_red())
  embed = discord.Embed(title="Rolled 2d6", color=discord.Color.yellow()) #color can change to the characters selected color
  embed.add_field(name="Total", value=total, inline=False)

  for num, item in enumerate(lstDice):
    embed.add_field(name="Die " + str(num), value=item, inline=True)
  return embed


class CharacterView(discord.ui.View):

    character: Character
    on_edit: Callable

    def __init__(self, on_edit_:Callable):
        super().__init__()
        self.on_edit = on_edit_


    def update(self, char:Character):
        for item in self.children:
            self.remove_item(item)

        self.character = char

        # item = discord.ui.Item()
        btn_str = StatButton("STR", char.STR, lambda i: self.click(i, "STR", char.STR))
        btn_dex = StatButton("DEX", char.DEX, lambda i: self.click(i, "DEX", char.DEX))
        btn_con = StatButton("CON", char.CON, lambda i: self.click(i, "CON", char.CON))
        btn_int = StatButton("INT", char.INT, lambda i: self.click(i, "INT", char.INT))
        btn_wis = StatButton("WIS", char.WIS, lambda i: self.click(i, "WIS", char.WIS))
        btn_cha = StatButton("CHA", char.CHA, lambda i: self.click(i, "CHA", char.CHA))

        btn_name = DynButton(label=char.name, style=discord.ButtonStyle.primary, callback=self.edit)
        self.add_item(btn_name)

        self.add_item(btn_str)
        self.add_item(btn_dex)
        self.add_item(btn_con)
        self.add_item(btn_int)
        self.add_item(btn_wis)
        self.add_item(btn_cha)

        # Needs to be in a modal
        # txt_name = TextInput[View](label="label")
        # self.add_item(txt_name)

    async def click(self, interaction:Interaction, name:str, stat:Stat):
        # print("CLICK")
        # How to edit existing message
        # await interaction.response.edit_message(content="Clicked " + stat.name, view=self)

        # How to add a new message
        embed = chaRoll(stat.to_bonus(), name)
        await interaction.response.send_message(embed = embed)


    async def edit(self, interaction:Interaction):
        print("EDIT")
        modal = CharacterEdit(self.character)
        modal.on_submit = self.edited # type: ignore
        await interaction.response.send_modal(modal)


    async def edited(self, interaction:Interaction):
        print("EDITED", interaction.data)

        comps = interaction.data.get("components")[0].get("components") # type: ignore
        name = comps[0].get("value")
        print("NAME", name)
        self.character.name = name
        self.update(self.character)

        self.on_edit()
        await interaction.response.edit_message(content="Edited!", view=self)


# class CharacterEdit(Modal, title="Edit Character"):

#     character:Character

class CharacterEdit(Modal, title='Edit Character'):
    # name = TextInput[View](label='Name')
    # str = TextInput[View](label='STR')
    # dex = TextInput[View](label='DEX')
    # con = TextInput[View](label='CON')
    # int = TextInput[View](label='INT')
    # wis = TextInput[View](label='WIS')
    # cha = TextInput[View](label='CHA')

    def __init__(self, char:Character):
        super().__init__()
        # self.character = char

        name_input = TextInput[View](label='Name', placeholder='Dargon McCharacter', default=char.name)
        self.add_item(name_input)

        dex_input = TextInput[View](label='DEX', default=str(char.DEX.value))
        str_input = TextInput[View](label='STR', default=str(char.STR.value))

        self.add_item(dex_input)
        self.add_item(str_input)




class StatButton(discord.ui.Button):

    stat: Stat
    name: str

    def __init__(self, name:str, stat:Stat, click:Callable):
        super().__init__(
            label=name + ": " + bonus_str(stat),
            style=discord.ButtonStyle.success,
        )
        self.callback = click # type: ignore
        self.name = name
        self.stat = stat




    # async def click(self, interaction:Interaction):
    #     await interaction.response.edit_message(content="Clicked: " + self.stat.encode(), view=self)



def bonus_str(stat:Stat) -> str:
    if stat.to_bonus() >=0:
        return "+" + str(stat.to_bonus())
    else:
        return str(stat.to_bonus())
    



#   def add_buttons(self, moves:list[Move]):
#     self.moves = moves
#     for move in moves:
#       button = lib.component.DynButton(label=move.name, style=discord.ButtonStyle.green)
#       button.set_callback(self.callback)
#       self.add_item(button)

#   async def callback(self, interaction:Interaction):
#     print("CALLED!", self)

#     children:List[lib.component.DynButton] = self.children # type: ignore
    
#     # Disable all buttons
#     for item in children:
#         item.disabled = True

#     # Update the message
#     await interaction.response.edit_message(content="Buttons are now disabled", view=self)

#   async def on_timeout(self) -> None:
#     # await self.disable_all_items()
#     # if self.message:
#     #   await self.message.channel.send("Timeout")
#     # else:
#     print("Timeout!")

#   @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
#   async def hello(self, interaction:Interaction, button: discord.ui.Button):
#     # This sends another message
#     print("- CLICK HELLO")
#     await interaction.response.send_message("Hello: " + character.name)
#     print("- AFTER HELLO")

  # @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
  # async def cancel(self, interaction:Interaction, button: discord.ui.Button):
  #   print("- CLICK CANCEL")
  #   await self.disable_all_items()
  #   await interaction.response.edit_message(view=self)

