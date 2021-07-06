# 檔名：xkcd.py


import discord
from discord.ext import commands
import os
import requests
from bs4 import BeautifulSoup
import random
a = 2481
stri='iuuqt;00tvqs/mjol0jm5TY'
s = 'https://xkcd.com/'
urlst = []
for _ in range(1, 2481):
    urlst.append(s+str(_))
while 1:  # 偵測新漫畫
    res = str(requests.get(s+str(a+1)))
    if '200' in res:
        urlst.append(s+str(a+1))
        a+=1
    else:
        break
class Xkcd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = '''
    Watch comics.
    $xkcd a [篇目]
    ex: xkcd a 1
        xkcd a 1,2
        xkcd a 1-3
    $xkcd r 數目:隨機看
    $xkcd t ...
    
 
    
    ''', brief = "Watch comics.")
    async def xkcd(self, ctx,method=None,page=None):
        print(method)
        print(page)
        if method == 'a':
            if page==None:
                await ctx.send("error range")
                return 
            if '-' in page:
                multilist = list(map(int, page.split('-')))
                if multilist[0] > a or multilist[0] <= 0 or multilist[1] > a or multilist[1] <= 0:
                    print('無此漫畫!!')
                    await ctx.send('Can not find this comic')
                else:
                    if len(multilist)>5:
                            print('e04太多了')
                            return
                    errcount=0
                    lst = []
                    for _ in range(multilist[0], multilist[1]+1):
                        lst.append(str(_))
                    for i in lst:
                        r = requests.get(s+i)
                        errcount=0
                        soup = BeautifulSoup(r.text, "html.parser")
                        result = soup.select('#comic > img')
                        if result == []:
                            result = soup.select('#comic > a > img')
                        if result == []:
                            errcount+=1
                            print(str(errcount)+"errors")
                        else:
                            re = 'https:'+result[0].attrs['src']
                            e = discord.Embed()
                            e.set_image(url=re)
                            await ctx.send(embed=e)
            elif ',' in page:
                errcount=0
                multilist = page.split(',')
                if '' in multilist:
                        multilist.remove('')
                for i in multilist:
                    if int(i) > a or int(i) <= 0:
                        print('Can not find this comic')
                        await ctx.send('Can not find this comic')
                    else:
                        if len(multilist)>5:
                            print('e04太多了')
                            return
                        r = requests.get(s+i)
                        errcount=0
                        soup = BeautifulSoup(r.text, "html.parser")
                        result = soup.select('#comic > img')
                        if result == []:
                            result = soup.select('#comic > a > img')
                        if result == []:
                            errcount+=1
                            print(str(errcount)+"errors")
                        else:
                            re = 'https:'+result[0].attrs['src']
                            e = discord.Embed()
                            e.set_image(url=re)
                            await ctx.send(embed=e)
            elif page.isdigit():
                if int(page) > a or int(page) <= 0:
                    print('Can not find this comic')
                    await ctx.send('Can not find this comic')
                else:
                    r = requests.get(s+page)
                    errcount=0
                    soup = BeautifulSoup(r.text, "html.parser")
                    result = soup.select('#comic > img')
                    if result == []:
                        result = soup.select('#comic > a > img')
                    if result == []:
                        errcount+=1
                        print(str(errcount)+" errors")
                        await ctx.send(str(errcount)+" errors")
                    else:
                        re = 'https:'+result[0].attrs['src']
                        e = discord.Embed()
                        e.set_image(url=re)
                        await ctx.send(embed=e)
            else:
                await ctx.send('input error')
        elif method == 'r':
            flag=True
            try:
                if int(page)<0 or int(page)>a:
                    await ctx.send('input error')
            except:
                await ctx.send("require a number")
            else:
                new_url = urlst
                random.shuffle(new_url)
                for _ in range(int(page)):
                    r = requests.get(new_url[_])
                    errcount=0
                    soup = BeautifulSoup(r.text, "html.parser")
                    result = soup.select('#comic > img')
                    new_url.remove(new_url[_])
                    if result == []:
                        result = soup.select('#comic > a > img')
                    if result == []:
                        errcount+=1
                        print(str(errcount)+" errors")
                        await ctx.send(str(errcount)+" errors")
                    else:
                        re = 'https:'+result[0].attrs['src']
                        e = discord.Embed()
                        e.set_image(url=re)
                        if flag == False:
                            print('aaa')
                        await ctx.send(embed=e)
        elif method=='t':
            #不知道會不會看到
            await ctx.send(''.join([(chr(ord(k)-1)) for k in stri]))

        else:
            await ctx.send('method error')
                
def setup(bot):
    bot.add_cog(Xkcd(bot))
