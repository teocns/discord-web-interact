from discord.ext import commands
import discord

import logging
from contexts import InteractionChannelContext, manager

log = logging.getLogger(__name__)

class BaseBOT(commands.Bot):


    ctx_manager: manager.ContextsManager = manager.ContextsManager()

    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.default(),
        )

    @staticmethod
    def launch(token):
        b = BaseBOT()
        b.run(token)
        return b

    async def on_ready(self):
        log.info(f"BOT {self.user.display_name} successfully connected to Discord servers") 

        self.ctx_manager.register_many(
            InteractionChannelContext,
            *self.guilds
        )
