from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # Creates server config
        guild_id = guild.id

        from data import SQLServer_config
        SQLServer_config.new_server(guild_id)

        from data import SQLServer_curses
        SQLServer_curses.initiate_server(guild_id)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        guild_id = guild.id

        # Deletes server config
        from data import SQLServer_config
        SQLServer_config.delete_server(guild_id)

        # Deletes curses to save space
        from data import SQLServer_curses
        SQLServer_curses.delete_server(guild_id)

        # Deletes cursed users to save space
        from data import SQLUser_cursed
        SQLUser_cursed.cure_server(guild_id)


def setup(client):
    client.add_cog(Guilds(client))
