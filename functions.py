from client import client
import discord
import logging


log = logging.getLogger(__name__)



async def create_interact_role(guild: discord.Guild):
    """Create the main Interact-Winner role
    """

    ROLE_NAME = 'Interact-Winner'
    # If role doesn't already exists, create
    if (discord.utils.get(guild.roles, name=ROLE_NAME)) is None:
        guild.create_role(name=ROLE_NAME, colour=discord.Colour(0x000000))
        log.info("Created Role %s on guild %s", ROLE_NAME, guild.name)





async def create_interact_channel(guild: discord.Guild):
    CHANNEL_NAME = 'Interact with me'
    if (discord.utils.get(guild.channels, name=CHANNEL_NAME)) is None:
        guild.create_voice_channel(name=CHANNEL_NAME)
        log.info("Created Channel %s on guild %s", CHANNEL_NAME, guild.name)
