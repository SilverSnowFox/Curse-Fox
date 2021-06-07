import discord
from discord.ext import commands


class Messages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(alises=["Cure", "cure"])
    async def curse_user(self, ctx, arg):
        # Checks if have agreed to terms
        # Curses the user with an existing curse
        # Check if user not cursed
        # Check if settings allow to curse
        # -> Only admin at first
        # -> Need to enable if for certain roles or for all
        pass

    @commands.Cog.listener()
    async def on_message(self, guild=discord.Guild, message=None):
        if guild is None:
            pass
        # Checks if user is cursed
        # Checks that not a DM and get info from guild
        # - If yes, gets data and creates webhook
        # - If no, ignore
        pass


def setup(client):
    client.add_cog(Messages(client))
