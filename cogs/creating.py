import discord
from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Create", "create"])
    async def create_curse(self, ctx, arg):
        # Check that server has agreed to terms
        # Check how to avoid SQL injection attacks
        # Creates a curse arg, single word
        # Check that not profanity
        # Check that doesn't already exists
        pass

    @commands.command(aliases=["Delete"])
    async def delete_curse(self, ctx, arg):
        # Checks that server has agreed to terms
        # Admin lvl command
        # Deletes a curse, if exists
        pass


def setup(client):
    client.add_cog(Guilds(client))
