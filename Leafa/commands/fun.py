import discord
from discord.ext import commands


class Fun(commands.Cog):
    '''Works with fun commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'hug', help = 'Envia uma foto no aleatória. Não requer argumento. (Em manutenção)')
    async def hug(self, ctx, user):
        url_image = 'https://tenor.com/view/abraço-hug-anime-gif-14903934'

        await ctx.send(f'**{ctx.author.name}** abraçou **{user}**')
        await ctx.send(url_image)


def setup(bot):
    bot.add_cog(Fun(bot))
