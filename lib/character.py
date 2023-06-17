import discord
from discord import Interaction
from lib.dungeon_world import Character
from lib.component import DynButton

class CharacterView(discord.ui.View):

    character: Character

    def set_character(self, character:Character):
        self.character = character
        print("CHARACTER!")

        # item = discord.ui.Item()
        str = DynButton(label="str", style=discord.ButtonStyle.success)
        str.set_callback(lambda i: self.click(i))
        self.add_item(str)

    async def click(self, interaction:Interaction):
        print("CLICK " + str(self.character.STR.value))
        await interaction.response.edit_message(content="Clicked Strength", view=self)





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

