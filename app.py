from twitchio.ext import commands
from src.bot import Bot
from dotenv import load_dotenv
from threading import Thread
from time import sleep

CHANNEL = "isaukywhite"

load_dotenv()

class BotTwitch(Bot):
    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Olá, {ctx.author.name}! Bem-vindo ao chat! 😊")
    
    @commands.command(name="projects")
    async def projects(self, ctx):
        await ctx.send(f"Visualize os projetos para os streamers em twitchprojects.com")
        

async def loop_message(bot: Bot):
    while True:
        sleep(60)
        for channel in bot.connected_channels:
            await channel.send("Olá, pessoal! 😊, utilize o comando !projects para conhecer um pouco do nosso projeto!")
        

if __name__ == "__main__":
    channels = [CHANNEL]
    bot = BotTwitch(channels)
    tr = Thread(target=loop_message, args=(bot,))
    tr.start()
    bot.run()
