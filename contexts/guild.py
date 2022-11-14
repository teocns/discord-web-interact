import discord
import logging
from . import IBotContext

from guild.manager import GuildManager

import discord

log = logging.getLogger(__name__)


    
class GuildContext(IBotContext):
    """
    Context for a Guild
    """

    guild: discord.Guild

    def __init__(
        self,
        guild: discord.Guild,
    ) -> None:
        self.guild = guild


    async def on_ready(self):
        pass


    async def on_message(self, message):
        pass    