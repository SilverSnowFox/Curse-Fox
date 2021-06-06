import discord
from discord.ext import commands


class Cure(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Cure"])
    async def cure(self, ctx, member=discord.Member):
        # Curses a user
        # -> Self cure enabled by default
        # -> Other cursed can cure by default
        # -> All non cursed can cure
        pass

    @commands.command(aliases=["Masscure", "masscure"])
    async def mass_cure(self, ctx):
        # Admin
        # Cures all users in the server
        pass


def setup(client):
    client.add_cog(Cure(client))
