from twitchio.ext import commands
from src.bot import Bot
from dotenv import load_dotenv

CHANNEL = "isaukywhite"

load_dotenv()

class BotTwitch(Bot):
    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Olá, {ctx.author.name}! Bem-vindo ao chat! 😊")

if __name__ == "__main__":
    channels = [CHANNEL]
    bot = BotTwitch(channels)
    bot.run()
