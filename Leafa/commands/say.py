from discord.ext import commands


class Say(commands.Cog):
    '''Controls what the Leafa will say'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'say', help = 'Faz a Leafa dizer algo. Argumentos: Mensagem. (Somente para Adms)')
    async def say(self, ctx, *message):
        '''response = ' '.join(message)
        await ctx.channel.send(response)'''
        await ctx.channel.send('Este comando está desabilitado no momento! Volte mais tarde hehehe.')
    
    @commands.command()
    async def cap(self, ctx, *message):
        message = ' '.join(message)
        response =  f'''{message}
O **Capítulo 11** de **Who Invited You?** corram lá!
https://tsukimangas.com/leitor/5141/252636/who-invited-you/11#1
        '''
        await ctx.channel.send(response)


def setup(bot):
    bot.add_cog(Say(bot))