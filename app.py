from twitchio.ext import commands
from src.bot import Bot
from dotenv import load_dotenv
from threading import Thread
from time import sleep
import asyncio
import random

CHANNEL = "isaukywhite"

joins = {}

load_dotenv()

class BotTwitch(Bot):
    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Olá, {ctx.author.name}! Bem-vindo ao chat! 😊")
    
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
            await ctx.send(f"{user_name}, você não pode realizar essa ação no canal {channel_name}!")
            return
        if channel_name not in joins:
            joins[channel_name] = []
        if len(joins[channel_name]) == 0:
            await ctx.send("Nenhum participante na lista!")
        else:
            winner = random.choice(joins[channel_name])
            await ctx.send(f"O vencedor é: {winner}")

async def loop_message(bot: Bot):
    while True:
        sleep(300)
        for channel in bot.connected_channels:
            await channel.send("Olá, pessoal! 😊, utilize o comando !projects para conhecer um pouco do nosso projeto!")
        
def start_loop(bot: Bot):
    asyncio.run(loop_message(bot))

if __name__ == "__main__":
    channels = [CHANNEL]
    bot = BotTwitch(channels)
    tr = Thread(target=start_loop, args=(bot,))
    tr.start()
    bot.run()
