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
    async def print(self, ctx,):

        
        await ctx.send(str(mes1)+str(mes2)+str(mes3)+str(mes4))


def setup(bot):
    bot.add_cog(print(bot))
