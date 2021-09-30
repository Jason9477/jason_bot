# 檔名：covid.py
# 功能：印出疾管署提供台灣疫情的統計數字

import discord
from discord.ext import commands


class print(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help = '''
            print
         ''',
        brief = "print"
    )
    async def print(self, ctx):

        
        await ctx.send()


def setup(bot):
    bot.add_cog(print(bot))
