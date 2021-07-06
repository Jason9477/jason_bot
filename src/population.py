# 檔名：population.py
# 功能：印出各個國家的人口數據

from unittest import result
import discord
from discord.ext import commands
# import asyncio
import requests
from bs4 import BeautifulSoup
import time

class Population(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
        help = '''

            印出各個國家的人口數據

            $population
            等待
            
            輸入一或多個數字並以逗號分隔

         ''',
        brief = "Print world's population statics"
    )
    async def population(self, ctx):
        poplist=['United_States_of_America_(USA)', 'China', 'Japan', 'Germany', 'United_Kingdom_(UK)', 'India', 'France', 'Italy', 'Canada', 'Republic_of_Korea', 'Russian_Federation', 'Australia', 'Brazil', 'Spain', 'Mexico', 'Indonesia', 'Netherlands', 'Switzerland', 'Saudi_Arabia', 'Turkey', 'Taiwan_(Republic_of_China)', 'Iran', 'Poland', 'Sweden', 'Belgium', 'Thailand', 'Nigeria', 'Austria', 'Ireland', 'Israel', 'Norway', 'Argentina', 'Philippines', 'United_Arab_Emirates', 'Egypt', 'Denmark', 'Malaysia', 'Singapore', 'Hong_Kong', 'Vietnam', 'Bangladesh', 'South_Africa', 'Chile', 'PAkistan', 'Finland', 'Colombia', 'Romania', 'Czech_Republic', 'Portugal', 'New_Zealand']
        await ctx.send("選擇下面一或多個國家或是輸入world查看整個世界(資料可能有延遲）")
        e=discord.Embed()
        e.set_image(url='https://raw.githubusercontent.com/Jason9477/7/master/New%20Project.png')
        await ctx.send(embed=e)
        country=await self.bot.wait_for('message',timeout=300.0)
        c_list=[]
        input_list=country.content.split(',')
        print(input_list)
        for _ in range(len(input_list)):

            try:
                if int(input_list[_])>50 or int(input_list[_])<1:
                    await ctx.send('input errorrr')
                    return 
                else:
                    n=poplist[input_list[_]-1]

                    url='https://countrymeters.info/cn/'+n
            except:
                if input_list[_]=='world':
                    n='world'
                    url='https://countrymeters.info/cn/world'
                else:
                    await ctx.send('input error')
                    return 
            c_list.append(n)
            r=requests.get(url)
            print(url)
            soup=BeautifulSoup(r.text,"html.parser")

            results=soup.select("#cp1")
            await ctx.send(n+'\'s static')


            text = [[]]*len(input_list)
            data=['目前人口','目前男性人口','目前女性人口','目前女性人口','目前女性人口','今年出生人數','今天出生人數','今年死亡人數','今天死亡人數','今年淨遷移','今天淨遷移','今年人口增長','今天人口增長']

            for k in [i for i in range(13) if i!=3 and i!=4]:
                
                results=soup.find(id="cp"+str(k+1)).text
                results=str(results).replace(' ',',')
                text[_].append(f'{data[k]}: {results}人')

            await ctx.send('\n'.join(text[_]))
            if len(input_list)!=1 and _!=len(input_list)-1:
                await ctx.send('==========================')
        flag=True
        while flag==True:
            flag=False
            await ctx.send('要將查詢資料存下來嗎[y/n]')
            yn=await self.bot.wait_for('message',timeout=300.0)
            if yn.content=='y' or yn.content=='yes':
                localtime = time.asctime( time.localtime(time.time()) )
                with open('output.txt', 'wt') as f:
                    f.write(localtime+'\n')
                    for i in range(len(input_list)):
                        f.write(c_list[i]+'\'s static')
                        print(c_list[i])
                        for _ in range(11):
                            f.write('\n'+text[i][_])
                        if i!=len(input_list)-1:
                            f.write('\n=============================\n')
                
                await ctx.send(file=discord.File('output.txt'))
                return
            elif yn.content=='n' or yn.content=='no':
                await ctx.send("ok")

                return
            else:
                flag=True
    @commands.command(help='''印出人口數排名前幾名國家數據
                              $toppop [number] 
                              1<=[number]<=20''',brief="Print top population country's statics")
    async def toppop(self,ctx,num):
        try:
            if int(num)<=20 and int(num)>=1:
                    r=requests.get("https://countrymeters.info/cn")
                    soup=BeautifulSoup(r.text,"html.parser")

                    results=soup.select("div.review:nth-child(5) > table:nth-child(2)")[0].find_all("td")
                    await ctx.send("country".ljust(40)+"population".center(40)+"rate".rjust(40))
                    for _ in range(int(num)):
                        result1=results[5*_+2].find("a").attrs['href'].split("/")[-1]
                        result2=results[5*_+3].text.replace(" ",",")
                        result3=results[5*_+4].text
                        await ctx.send(result1.ljust(50) + result2.center(50)+result3.rjust(50))
            else:
 
                await ctx.send("number out of range")
        except:
            await ctx.send("input error")
        
 

def setup(bot):
    bot.add_cog(Population(bot))
