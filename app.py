from twitchio.ext import commands
from src.bot import Bot
from dotenv import load_dotenv

CHANNEL = "isaukywhite"

load_dotenv()

class BotTwitch(Bot):
    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Olá, {ctx.author.name}! Bem-vindo ao chat! 😊")
    
    @commands.command(name="projects")
    async def isauky(self, ctx):
        await ctx.send(f"Visualize os projetos para os streamers em https://twitchprojects.com")

if __name__ == "__main__":
    channels = [CHANNEL]
    bot = BotTwitch(channels)
    bot.run()
