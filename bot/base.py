from discord.ext import commands
import discord

import logging
from contexts.manager import BotContextsManager
from contexts.interaction_channel import InteractionChannelContext
from .client import BotClient


log = logging.getLogger(__name__)

class BOT(BotClient):


    ctx_manager: BotContextsManager

    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.default(),
        )

    
        self.ctx_manager = BotContextsManager(self)

    @staticmethod
    def launch(token):
        b = BOT()
        b.run(token)
        return b

    async def on_ready(self):
        log.info(f"BOT {self.user.display_name} successfully connected to Discord servers") 
        for guild in self.guilds:
            context = InteractionChannelContext(guild)
            self.ctx_manager.register(context)
            await context.on_ready()
        