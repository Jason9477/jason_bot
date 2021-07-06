# 檔名：news.py
# 功能：印出各個國家的人口數據


import discord
from discord.ext import commands
# import asyncio
import requests
from bs4 import BeautifulSoup


class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help = '''
            查看即時新聞from tvbs
         ''',
        brief = ":Print latest news from tvbs"
    )
    async def tvbs(self, ctx):
        news_type=['politics','local','world','health','entertainment','life','money','tech','travel','sports']
        await ctx.send("想要查看什麼類型的新聞")
        await ctx.send("1.要聞\n2.社會\n3.全球\n4.健康\n5.娛樂\n6.生活\n7.理財房地產\n8.科技\n9.食尚\n10.運動")
        
        flag=True
        while flag==True:
            flag=False
            try:
                ans=await self.bot.wait_for('message',timeout=300.0)
            except:
                await ctx.send("輸入錯誤，請重新輸入1-10")
                flag=True
            if flag==False: 
                if int(ans.content)<=10 and int(ans.content)>=1:
                    r=requests.get("https://news.tvbs.com.tw/realtime/"+news_type[int(ans.content)-1])
                    soup=BeautifulSoup(r.text,"html.parser")
                    results=[]
                    re=[]
                    k=0
                    for _ in [1,2,3,5,6,7,8,10,11,12]:
                        re.append(soup.select("body > div.container > main > div > article > div.news_list > div.list > ul > li:nth-child("+str(_)+")>a")[0].attrs['href'])
                        results.append(soup.select("body > div.container > main > div > article > div.news_list > div.list > ul > li:nth-child("+str(_)+") > a > h2")[0].text)
                        await ctx.send(str(k+1)+"."+results[k].replace("\\u3000"," "))
                        k+=1
                        
                    await ctx.send("輸入數字查看完整報導,可連續q或quit離開")
                    flag3=True
                    while flag3==True:
                        ans2=await self.bot.wait_for('message',timeout=300.0)
                        try:
                            if int(ans2.content)<=10 and int(ans2.content)>=1:
                                await ctx.send("https://news.tvbs.com.tw"+re[int(ans2.content)-1])
                            else:
                                await ctx.send("input error")
                        except:
                            if 'q' in str(ans2.content):
                                await ctx.send("quit")
                                flag3=False
                else:
                    await ctx.send("輸入錯誤，請輸入1-10")
                    flag=True
        
    @commands.command(help = "查看即時新聞from yahoo",brief = ":Print latest news from yahoo")
    async def yahoo(self, ctx):

        news_type=["","entertainment","world","politics","society","finance","sports","lifestyle","technology","health"]
        await ctx.send("想要查看什麼類型的新聞")
        await ctx.send("1.焦點\n2.娛樂\n3.國際\n4.政治\n5.社會地方\n6.財經\n7.體育\n8.生活\n9.科技\n10.健康")

                
        flag=True
        while flag==True:
            flag=False
            try:
                answer=await self.bot.wait_for('message',timeout=300.0)
                
            except:
                await ctx.send("輸入錯誤，請重新輸入1-10")
                flag=True
            if flag==False:
                try:
                    ans10=int(answer.content)
                except:
                    await ctx.send("quit!!")
                if int(answer.content)<=10 and int(answer.content)>=1:
                    r=requests.get("https://tw.news.yahoo.com/"+news_type[int(answer.content)-1])
                    soup=BeautifulSoup(r.text,"html.parser")
                    results=[]
                    re=[]
                    k=0
                    a=0
                    n=0
                    for _ in range(1,100):
                        try:
                            re.append(soup.select("li.js-stream-content:nth-child("+str(_)+") > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(2) > a:nth-child(1)")[0].attrs['href'])
                            results.append(soup.select("li.js-stream-content:nth-child("+str(_)+") > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(2) > a:nth-child(1)")[0].text)
                            await ctx.send(str(k+1)+"."+results[k])
                            k+=1
                        except:

                            k=k
                        if k==10:
                            break
                    await ctx.send("輸入數字查看完整報導，可連續q或quit離開")
                    flag2=True
                    while flag2==True:
                        
                        ans3=await self.bot.wait_for('message',timeout=300.0)
                        try:
                            if int(ans3.content)<=10 and int(ans3.content)>=1:
                                await ctx.send("https://tw.news.yahoo.com"+re[int(ans3.content)-1])
                                flag2=True
                                
                            else:
                                await ctx.send("quit")
                                
                        except:
                            if 'q' in str(ans3.content):
                                await ctx.send("quit")
                                flag2=False
                            else:
                                await ctx.send("input error")
                        

                else:
                    await ctx.send("輸入錯誤，請輸入1-10")
                    flag=True

                    
                    
                
                
            
    
       
def setup(bot):
    bot.add_cog(News(bot))
