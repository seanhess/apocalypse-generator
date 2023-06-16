import discord

class DynButton(discord.ui.Button):
    def set_callback(self, value):
        self.callback = value # type: ignore