from discord.guild import Guild

class GuildManager:

    guilds: dict[int, Guild] = {}

    def register(self, guild: Guild):
        self.guilds[guild.id] = guild