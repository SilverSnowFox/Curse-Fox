import discord
from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # Sends agreement on join
        # Once agreed, enables the rest
        pass

    @commands.Cog.listener()
    async def on_guild_leave(self, guild):
        # Deletes server data
        pass


def setup(client):
    client.add_cog(Guilds(client))
