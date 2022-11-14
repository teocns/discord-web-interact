
import discord







def on_guild_join(guild: discord.Guild):
    """This function is called when the bot joins a guild.

    Args:
        guild (discord.Guild): The guild the bot joined.
    """
    from functions import create_interact_role


    create_interact_role(guild)



