from discord.ext import commands


class Reactions(commands.Cog):
    '''Talk with Reactions'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == '👍':
            role = user.guild.get_role(882936366856568892)
            await user.add_roles(role)
        elif reaction.emoji == '😳':
            role = user.guild.get_role(882936389900050482)
            await user.add_roles(role)


def setup(bot):
    bot.add_cog(Reactions(bot))
