import requests

from discord.ext import commands


class Talks(commands.Cog):
    '''Talk with user'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help = 'Verifica o preço de um par da na binance. Argumentos: moeda, base.')
    async def binance(self, ctx, coin, base):
        name = ctx.author.name

        try:
            response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')

            data = response.json()
            price = data.get('price')
            print(price)

            if price:
                await ctx.send(f'O valor do par {coin}/{base} é {price}!')
            else:
                await ctx.send(f'O par {coin}/{base} é inválido! Não seja bobo **{name}**!')
        except Exception as error:
            await ctx.send(f'Eita... **{name}** alguma coisa deu errado!')


def setup(bot):
    bot.add_cog(Talks(bot))
