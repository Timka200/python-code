import discord
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='!',intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f'Вы вошли как {bot.user}')


@bot.command()
async def canhelp(ctx):
    with open(f'C:/Users/user/Desktop/bot for lesson/images/z1.jpg', 'rb') as a:
       picture = discord.File(a)
    await ctx.send(file=picture)
    await ctx.channel.send('Это мусор очень опасен для животных')
    await ctx.channel.send('Они могут застрять в них')
    await ctx.channel.send('Еси хочеш помоч природе, но не знаешь как. Напиши каманду:!protect ')

@bot.command()
async def protect(ctx):
    with open(f'C:/Users/user/Desktop/bot for lesson/images/z2.jpg', 'rb') as b:
       picture = discord.File(b)
    await ctx.send(file=picture)
    await ctx.channel.send('!!!Советы!!!')
    await ctx.channel.send('1)Надо садить деревья, убирать мусар')
    await ctx.channel.send('2)Не кидать мусар и.т.д')
    with open(f'C:/Users/user/Desktop/bot for lesson/images/z3.jpg', 'rb') as c:
       picture = discord.File(c)
    await ctx.channel.send('Дальше тут : https://turclub-pik.ru/blog/chto-ya-mogu-sdelat-dlya-ehkologii-30-sposobov/ ')

@bot.command()
async def links(ctx):
    await ctx.channel.send('Сылки:')
    await ctx.channel.send('1)Узнать больше : https://turclub-pik.ru/blog/chto-ya-mogu-sdelat-dlya-ehkologii-30-sposobov/')
    await ctx.channel.send('2)Еще информация : https://elle.ua/60-let-krasoty/act-beautiful-10-sposobov-sokhranit-nashu-planetu-kotorye-mozhet-delat-kazhdyj/')
    await ctx.channel.send('Желаю удачи')

@bot.command()
async def Help(ctx):
    await ctx.channel.send('!!Help!!')
    await ctx.channel.send('1)Сохронения природы = !canhelp')
    await ctx.channel.send('2)Еще информация = !protect')
    await ctx.channel.send('3)Сылки = !links')

bot.run('MTEwNjI2MTU2ODE2Mjg5Mzk5Ng.GsEfLv.dXnp22dDFqMgdCJLoQFrz_tXKCPTcUX3Dt7iEs')
