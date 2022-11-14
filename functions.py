import discord
import logging
from config import VOICE_CHANNEL_REQUIRED_ROLE, VOICE_CHANNEL_NAME

log = logging.getLogger(__name__)



async def create_interact_role(guild: discord.Guild):
    """Create the main Interact-Winner role
    """
    
    # If role doesn't already exists, create
    if (discord.utils.get(guild.roles, name=VOICE_CHANNEL_REQUIRED_ROLE)) is None:
        await guild.create_role(name=VOICE_CHANNEL_REQUIRED_ROLE, colour=discord.Colour(0x000000))
        log.info("Created Role [%s] on guild [%s]", VOICE_CHANNEL_REQUIRED_ROLE, guild.name)





async def create_interact_channel(guild: discord.Guild):
    if (discord.utils.get(guild.channels, name=VOICE_CHANNEL_NAME)) is None:
        # Create a private voice channel where only users with the Interact-Winner role can join
        
        await guild.create_voice_channel(
            VOICE_CHANNEL_NAME, 
            overwrites={
                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                guild.me: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                discord.utils.get(guild.roles, name=VOICE_CHANNEL_REQUIRED_ROLE): discord.PermissionOverwrite(connect=True, view_channel=True)
            }
        )
        log.info("Created Channel [%s] on guild [%s]", VOICE_CHANNEL_NAME, guild.name)
