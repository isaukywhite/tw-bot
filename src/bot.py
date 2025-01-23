from twitchio.ext import commands
from datetime import datetime
import os
import requests

def getenv(key) -> str:
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Variável de ambiente {key} não encontrada!")
    return value

class Bot(commands.Bot):
    def __init__(self, channels: list[str]):
        self.TOKEN = getenv("TOKEN")
        self.BOT_NICK = getenv("BOT_NICK")
        self.CLIENT_ID = getenv("CLIENT_ID")
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
        now = datetime.now()
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} => {message.channel.name} => {message.author.name}: {message.content}")
        await self.handle_commands(message)
        
    def verify_is_online(self, channel: str) -> bool:
        url = f'https://api.twitch.tv/helix/streams?user_login={channel}'
        response = requests.get(
            url,
            headers={
                "Authorization": "Bearer " + self.TOKEN.split(":")[1],
                "Client-Id": self.CLIENT_ID,
            }
        )
        return response.json()["data"] != []