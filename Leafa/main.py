import os

from decouple import config
from discord.ext import commands


bot = commands.Bot('!')


'''def load_cogs(bot):
    bot.load_extension('manager')
    bot.load_extension('tasks.dates')

    for file in os.listdir('commands'):
        if file.endswith('.py'):
            cog = file[:-3]
            bot.load_extension(f'commands.[cog')

load_cogs(bot)'''

#Nota: Depois deixar as importações automáticas.
bot.load_extension('manager')

bot.load_extension('commands.cryptos')
bot.load_extension('commands.images')
bot.load_extension('commands.reactions')
bot.load_extension('commands.say')
bot.load_extension('commands.smarts')
bot.load_extension('commands.talk')

bot.load_extension('tasks.dates')

TOKEN = config('TOKEN')
bot.run(TOKEN)