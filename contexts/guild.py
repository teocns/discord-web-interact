import discord
import logging


from guild.manager import GuildManager

import discord

log = logging.getLogger(__name__)


    
class GuildContext:
    __manager = GuildManager()

    @property
    def guilds_manager(self):
        return self.__manager

    def __init__(
        self,
        GUILD: discord.Guild,
    ) -> None:
       pass


    async def on_ready(self):
        # Iterate GUILDS
        for guild in self.client.guilds:
            print(guild.name)
            self.manager.register(guild)



    async def on_message(self, message):
        super().on_message(message)

        if message.author != self.client.user:
            self.manager.handle_message(message)
            