import discord
from discord import Interaction
from discord.ui import TextInput, View
from lib.dungeon_world import Character, Stat
from lib.component import DynButton
from typing import Callable

class CharacterView(discord.ui.View):

    character: Character

    def set_character(self, char:Character):
        self.character = char
        print("CHARACTER!")

        # item = discord.ui.Item()
        btn_str = StatButton("STR", stat=char.STR, click = lambda i: self.click(i, "STR", char.STR))
        self.add_item(btn_str)

        # Needs to be in a modal
        # txt_name = TextInput[View](label="label")
        # self.add_item(txt_name)

    async def click(self, interaction:Interaction, name:str, stat:Stat):
        print("CLICK " + name + " " + bonus_str(stat))
        await interaction.response.edit_message(content="Clicked Strength", view=self)


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

