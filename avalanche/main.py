import discord
from discord.ext import commands

import time, os

#_-----------------_#

bot = discord.Client()
bot = commands.Bot(
      intents = discord.Intents().all()
      command_prefix = "nomore ",
)

#_-----------------_#

@bot.event
async def on_message(message):
      if message.embeds in message.content and message.author is not bot:
         try:
            try:
               await message.author.send(embed = discord.Embed(title = "Selfbot Detected", description = "You have been detected as a selfbot from a message in <#{}>".format(ctx.channel.id))
            except:
               # Couldnt DM
               print ("COULDNT DM {}".format(message.author)
            await message.author.ban(reason = "Selfbotting")
          except:
               print ("COULDNT BAN USER {}".format(message.author))

                      
bot.run(token, bot = True)
