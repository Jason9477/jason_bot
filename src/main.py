# 檔名：main.py
# 功能：主程式、監聽訊息、鏈結加入其他功能
# TODO：實作 unload, reload
import math
import discord
from discord.ext import commands
import os

# Bot object、設定指令開頭
bot = commands.Bot(command_prefix='$')
token = os.getenv("DISCORD_BOT_TOKEN")
# 從 token.txt 中讀取 token
# 使用 os.path.join() 在不同作業系統會以 / 或是 \ 連接路徑

extensions=['todo_list','picture','covid','weather','guess','currency','xkcd','population','news','print']
# 從 extensions.txt 中讀取現有功能，並加入那些功能

for _ in extensions:
    # 加入功能 (直接使用 Bot method: load_extension)
    bot.load_extension(_.strip('\n')) 

# 一開始準備就緒時會觸發
@bot.event
async def on_ready():
    print("Ready!")
    # 印出 bot 這個 user 的資訊
    print("User name:", bot.user.name)
    print("User ID:", bot.user.id)
    global ls
    ls=[]
# 監聽訊息，有訊息時會觸發
@bot.event
async def on_message(message):
    print(ls)

    # 檢查訊息是否是 bot 自己傳的
    if message.author.id == bot.user.id:
        return
    if message.content.lower().isdigit() and len(message.content.lower())==4:
        sum=0
        if message.content.lower()!=1324:
            for i in message.content.lower():
                if i==1 or i==2 or i==3 or i==4:
                    sum+=1
            await message.channel.send(str(sum)+'個正確')
        else:
            ls.append(message.author.id)

    if message.author.id != bot.user.id and message.author.id!=690742477086261266 and message.author.id not in ls:
        await message.delete()
        return
    if 'ban' in str(message.content.lower()):
        if int(str(message.content.lower()).split(' ')[1]) in ls:
            ls.remove(int(str(message.content.lower()).split(' ')[1]))
    if 'unban' in str(message.content.lower()):
        if int(str(message.content.lower()).split(' ')[1]) not in ls:
            ls.append(int(str(message.content.lower()).split(' ')[1]))
    if "生日快樂" in str(message.content.lower()):
        ls.append(message.author.id)
        print(ls)

    if message.author.id not in ls:
        await message.delete()
        await message.channel.send("祝謝承哲生日快樂啦")
    

    # 回應有 hello 的訊息
    if "hello" in message.content.lower():
        await message.channel.send("Hello~ Nice to meet you.") # Bot 傳送訊息
    lis=[]
    summ=0
    if '+' in message.content.lower() :
        lis=message.content.lower().split('+')
        for _ in lis:
            summ+=int(_)
        await message.channel.send(summ)
    if '*' in message.content.lower() :
        summ=1
        lis=message.content.lower().split('*')
        for _ in lis:
            summ*=int(_)
        await message.channel.send(summ)
    if '^'  in message.content:
        await message.channel.send(math.pow(int(message.content.split("^")[0]),int(message.content.split("^")[1])))



        

    # 回應 help 開頭的訊息
    if message.content.lower().startswith("help"):
        await message.channel.send("Enter commands starting with $ or enter $help for more information:)")

    # 加這行才可以用 commands
    await bot.process_commands(message)

# load extension 加入功能
# 使用者輸入 $load 時會觸發
@bot.command(help = "Load extension.", brief = "Load extension.")
async def load(ctx, extension): # extension: 使用者輸入要加入的功能
    try:
        bot.load_extension(extension.lower()) # load extension, lower() 因為檔名是小寫
        await ctx.send(f"{extension} loaded.") # Bot 傳送訊息
    except Exception as e:
        await ctx.send(e) # 若加入失敗印出錯誤訊息

# unload extension 卸載功能
@bot.command(help = "Un-load extension.", brief = "Un-load extension.")
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension.lower()) # load extension, lower() 因為檔名是小寫
        await ctx.send(f"{extension} unloaded.") # Bot 傳送訊息
    except Exception as e:
        await ctx.send(e) # 若加入失敗印出錯誤訊息
# reload extension 重新加入功能
@bot.command(help = "Re-load extension.", brief = "Re-load extension.")
async def reload(ctx, extension):
    try:
        bot.reload_extension(extension.lower()) # load extension, lower() 因為檔名是小寫
        await ctx.send(f"{extension} reloaded.") # Bot 傳送訊息
    except Exception as e:
        await ctx.send(e) # 若加入失敗印出錯誤訊息
bot.run(token) # 執行
