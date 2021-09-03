from discord.ext import commands


class Say(commands.Cog):
    '''Controls what the Leafa will say'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'say', help = 'Faz a Leafa dizer algo. Argumentos: Mensagem. (Somente para Adms)')
    async def say(self, rtx, *message):
        response = ' '.join(message)
        await rtx.channel.send(response)


def setup(bot):
    bot.add_cog(Say(bot))
