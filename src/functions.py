import discord
import logging
from services.config import Config
log = logging.getLogger(__name__)



INTERACT_CHANNEL_ROLENAME = Config.get('INTERACT_CHANNEL_ROLENAME')
INTERACT_CHANNEL_NAME = Config.get('INTERACT_CHANNEL_NAME')


async def create_interact_role(guild: discord.Guild):
    """Create the main Interact-Winner role"""
    
    # If role doesn't already exists, create
    if (discord.utils.get(guild.roles, name=INTERACT_CHANNEL_ROLENAME)) is None:
        await guild.create_role(name=INTERACT_CHANNEL_ROLENAME, colour=discord.Colour(0x000000))
        log.info("Created Role [%s] on guild [%s]", INTERACT_CHANNEL_ROLENAME, guild.name)





async def create_interact_voice_channel(guild: discord.Guild):
    if (discord.utils.get(guild.voice_channels, name=INTERACT_CHANNEL_NAME)) is None:
        # Create a private voice channel where only users with the Interact-Winner role can join
        
        await guild.create_voice_channel(
            INTERACT_CHANNEL_NAME, 
            overwrites={
                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                guild.me: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                discord.utils.get(guild.roles, name=INTERACT_CHANNEL_ROLENAME): discord.PermissionOverwrite(connect=True, view_channel=True)
            }
        )
        log.info("Created voice-channel [%s] on guild [%s]", INTERACT_CHANNEL_NAME, guild.name)


async def create_interact_text_channel(guild: discord.Guild):
    if (discord.utils.get(guild.text_channels, name=INTERACT_CHANNEL_NAME)) is None:
        # Create a private voice channel where only users with the Interact-Winner role can join
        
        await guild.create_text_channel(
            INTERACT_CHANNEL_NAME, 
            overwrites={
                guild.default_role: discord.PermissionOverwrite(send_messages=False, view_channel=False),
                guild.me: discord.PermissionOverwrite(send_messages=True, view_channel=True, manage_channels=True),
                discord.utils.get(guild.roles, name=INTERACT_CHANNEL_ROLENAME): discord.PermissionOverwrite(send_messages=True, view_channel=True)
            }
        )
        log.info("Created text-channel [%s] on guild [%s]", INTERACT_CHANNEL_NAME, guild.name)