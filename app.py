from twitchio.ext import commands
from src.bot import Bot
from dotenv import load_dotenv
from threading import Thread
import asyncio
import random
from src.database import Database
from src.daily_message import daily_message

joins = {}

load_dotenv()

class BotTwitch(Bot):
    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Olá, {ctx.author.name}! Bem-vindo ao chat! 😊")
        
    @commands.command(name="test")
    async def test(self, ctx: commands.Context):
        await ctx.send(f"{ctx.author.name} isso e apenas um teste!")
    
    @commands.command(name="projects")
    async def projects(self, ctx: commands.Context):
        await ctx.send(f"Visualize os projetos para os streamers em twitchprojects.com")
        
    @commands.command(name="join")
    async def join(self, ctx: commands.Context):
        channel_name = ctx.channel.name
        if channel_name not in joins:
            joins[channel_name] = []
        if ctx.author.name in joins[channel_name]:
            await ctx.send(f"{ctx.author.name} já está na lista de participantes!")
        else:
            joins[channel_name].append(ctx.author.name)
            await ctx.send(f"{ctx.author.name} entrou na lista de participantes!")
        
        
    @commands.command(name="list")
    async def list_join(self, ctx: commands.Context):
        channel_name = ctx.channel.name
        if channel_name not in joins:
            joins[channel_name] = []
        if len(joins[channel_name]) == 0:
            await ctx.send("Nenhum participante na lista!")
        else:
            await ctx.send(f"Lista de participantes: {joins[channel_name]}")
            
    @commands.command(name="lottery")
    async def lottery(self, ctx: commands.Context):
        channel_name = ctx.channel.name
        user_name = ctx.author.name
        if channel_name != user_name:
            return
        if channel_name not in joins:
            joins[channel_name] = []
        if len(joins[channel_name]) == 0:
            await ctx.send("Nenhum participante na lista!")
        else:
            winner = random.choice(joins[channel_name])
            await ctx.send(f"O vencedor é: {winner}")
            
    @commands.command(name="message")
    async def message(self, ctx: commands.Context):
        message = daily_message()
        while message == None:
            message = daily_message()
        await ctx.send(message)

async def loop_message(bot: Bot):
    for channel in bot.connected_channels:
        if not bot.verify_is_online(channel.name):
            continue
        message = daily_message()
        if message == None:
            message = "Olá, pessoal! 😊, utilize o comando !projects para conhecer um pouco do nosso projeto!"
        await channel.send(message)

async def main_loop(bot: Bot):
    while True:
        try:
            await loop_message(bot)
        except Exception as e:
            print(f"Erro: {e}")
        await asyncio.sleep(300)
        
        
def start_loop(bot: Bot):
    loop = asyncio.new_event_loop()
    loop.create_task(main_loop(bot))
    loop.run_forever()


if __name__ == "__main__":
    db = Database()
    result = db.query("SELECT name FROM users")
    channels = [user[0] for user in result]
    bot = BotTwitch(channels)
    tr = Thread(target=start_loop, args=(bot,))
    tr.start()
    bot.run()
