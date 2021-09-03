import discord
from discord.ext import commands


class Talks(commands.Cog):
    '''Talk with user'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'oi', help = 'Envia um Oi. Não requer nenhum argumento.')
    async def send_hello(self, ctx):
        name = ctx.author.name

        response = 'Olá **' + name + '**!'

        await ctx.send(response)
    
    @commands.command(name = 'segredo', help = 'Envia uma mensagem privado de teste no usuário. Não requer nenhum argumento.')
    async def secret(self, ctx):
        name = ctx.author.name
        try:
            await ctx.author.send('Teste 1!')
            await ctx.author.send('Teste 2!')
            await ctx.author.send('Teste 3!')
            await ctx.send(f'Eu te enviei algumas mensagens privadas **{name}**! Cheque sua DM!')
        except discord.errors.Forbidden:
            await ctx.send(f'**{name}** assim fica difícil! Não consegui te enviar uma mensagem porque a sua DM é fechada, habilite em (Opções / Privacidade).')


def setup(bot):
    bot.add_cog(Talks(bot))
