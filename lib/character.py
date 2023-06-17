import discord
from discord import Interaction
from discord.ui import TextInput, View, Modal
from lib.dungeon_world import Character, Stat
from lib.component import DynButton
from typing import Callable
from discord.components import ActionRow

class CharacterView(discord.ui.View):

    character: Character

    def set_character(self, char:Character):
        self.character = char
        print("CHARACTER!")

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
        # How to edit existing message
        # await interaction.response.edit_message(content="Clicked Strength", view=self)

        # How to add a new message
        await interaction.response.send_message("CLICKED " + name)


    async def edit(self, interaction:Interaction):
        print("EDIT")
        modal = Questionnaire()
        modal.on_submit = self.edited # type: ignore
        await interaction.response.send_modal(modal)
        print("AFTER")


    async def edited(self, interaction:Interaction):
        print("EDITED")
        await interaction.response.edit_message(content="Edited :)", view=self)





class Questionnaire(Modal, title='Questionnaire Response'):
    name = TextInput[View](label='Name')
    answer = TextInput[View](label='Answer', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)


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

