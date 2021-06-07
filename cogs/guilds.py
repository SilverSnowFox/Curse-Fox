from discord.ext import commands
from functions import SQLServer_config


class Guilds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # Creates server config
        guild_id = guild.id

        SQLServer_config.new_server(guild_id)

        from functions import SQLServer_curses
        SQLServer_curses.initiate_server(guild_id)

    @commands.Cog.listener()
    async def on_guild_leave(self, guild):
        guild_id = guild.id
        # Deletes server config
        SQLServer_config.delete_server(guild_id)

        # Deletes curses to save space
        from functions import SQLServer_curses
        SQLServer_curses.delete_server(guild_id)

        # Deletes cursed users to save space
        from functions import SQLUser_cursed
        SQLUser_cursed.cure_server(guild_id)


def setup(client):
    client.add_cog(Guilds(client))
