import discord
from .guild import GuildContext
from functions import create_interact_role, create_interact_text_channel, create_interact_voice_channel

class InteractionChannelContext(GuildContext):


    def __init__(
        self,
        guild
    ) -> None:
        self.guild = guild
        
    

    async def on_ready(self):
        await self.bootstrap()


    async def on_message(self, message):
        pass

    async def bootstrap(self):     
        await create_interact_role(self.guild)
        await create_interact_voice_channel(self.guild)
        await create_interact_text_channel(self.guild)
        
        