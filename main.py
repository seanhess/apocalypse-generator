import os
import bot

TOKEN=os.getenv("DISCORD_TOKEN")
bot.client.run(TOKEN if TOKEN else "")


