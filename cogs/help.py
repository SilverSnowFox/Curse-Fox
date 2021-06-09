import discord
from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Help"])
    async def help(self, ctx):
        # Help command
        # Try checking dictionary embed
        pass


def setup(client):
    client.add_cog(Guilds(client))
