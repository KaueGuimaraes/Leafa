from discord.ext import commands


class Smarts(commands.Cog):
    '''A lot of Smart Commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'calcular', help = 'Calcula uma expressão numérica. Argumentos: Expressão.')
    async def calculate_expression(self, ctx, *expression):
        expression = ''.join(expression)
        response = eval(expression)
        print(expression)

        await ctx.send('A resposta é: ' + str(response))
    
    @commands.command(name = 'noteimg', help = 'Comando adicional para facilitar imgnotes na Mudae. Argumentos: Páginas.')
    async def note_img(self, ctx, pages = 1):
        author = ctx.author.name

        if pages < 1:
            await ctx.send(f'Ei! **{author}** informe um número maior!')
        elif pages > 50:
            await ctx.send(f'Ei! **{author}** informe um número menor!')
        else:
            response = ' $ '
            for c in range(1, pages + 1):
                response = response + f'{c} $ '
            
            await ctx.send(response)


def setup(bot):
    bot.add_cog(Smarts(bot))
