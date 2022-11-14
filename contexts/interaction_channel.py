import discord
from .guild import GuildContext
from functions import create_interact_channel, create_interact_role

class InteractionChannelContext(GuildContext):


    async def __init__(
        self,
        guild
    ) -> None:
        self.guild = guild
        await self.bootstrap()
        
    async def bootstrap(self):
        # Attempts to create a role
        # If role already exists, it does nothing
        
        await create_interact_role(self.guild)
        await create_interact_channel(self.guild)
        