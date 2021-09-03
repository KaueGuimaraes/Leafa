import discord
from discord.ext import commands

from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound, CommandInvokeError


class Manager(commands.Cog):
    '''Mnage the Bot'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou pronta! Estou conectada como {self.bot.user}')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        name = message.author.name
        if message.author == self.bot.user:
            return
        
        if 'palavrão' in message.content:
            await message.channel.send(f'Por favor, {name} não ofenda os demais usuários!')

            await message.delete()
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument, CommandInvokeError)):
            await ctx.send(f'Por favor envie todos os argumentos necessários! Digite !help para ver os parâmetros de cada comando.')
        elif isinstance(error, CommandNotFound):
            await ctx.send('Esse comando não existe! Seu boboca! Digite !help para ver todos os comandos.')
        else:
            raise error



def setup(bot):
    bot.add_cog(Manager(bot))
