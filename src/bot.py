from twitchio.ext import commands
import os

def getenv(key) -> str:
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Variável de ambiente {key} não encontrada!")
    return value

class Bot(commands.Bot):
    def __init__(self, channels: list[str]):
        self.TOKEN = getenv("TOKEN")
        self.BOT_NICK = getenv("BOT_NICK")
        super().__init__(
            token=self.TOKEN,
            prefix="!",
            initial_channels=channels,
        )

    async def event_ready(self):
        print(f"Bot {self.BOT_NICK} conectado!")

    async def event_message(self, message):
        if not message.author:
            return
        if not message.author.name:
            return
        if message.author.name.lower() == self.BOT_NICK.lower():
            return
        await self.handle_commands(message)