import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["curses", "Curses"])
    async def curses_list(self, ctx):
        # Lists the curses
        pass

    @commands.command(aliases=["Cursed", "cursed"])
    async def cursed_users(self, ctx, arg=None):
        # If arg is none, lists amount of cursed users
        # If arg == all/All, lists all of the cursed users in an embed
        # If arg is a mention, return if user is cursed and with what
        # Embed
        pass

    @commands.command(aliases=["Latency"])
    async def latency(self, ctx):
        # Gets the bot latency
        pass

    @commands.command(aliases=["Agreement"])
    async def agreement(self):
        # Need to have admin perms to agree
        # Sends the agreement if haven't accepted, else sand that have
        pass


def setup(client):
    client.add_cog(Info(client))
