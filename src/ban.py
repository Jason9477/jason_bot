import discord
from discord.ext import commands
import main
class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = '''ban id ''', brief = "$ban id")
    async def ban(self, ctx,id):
        if int(id) not in main.ls:
            main.ls.remove(int(id))
    @commands.command(help = '''unban id ''', brief = "$unban id")
    async def unban(self, ctx,id):
        if int(id) in main.ls:
            main.ls.append(int(id))

def setup(bot):
    bot.add_cog(Ban(bot))