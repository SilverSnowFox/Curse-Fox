import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["EveryoneCure", "everyoneCure", "everyonecure"])
    @commands.has_permissions(administrator=True)
    async def everyone_can_cure(self, ctx, arg):

        if ctx.message.guild is None:
            await ctx.send("You can't use this command in DMs!")
            return

        # Checks for valid input
        answer = arg.lower()

        if answer != 'true' and answer != 'false':
            await ctx.send("Invalid argument. Please retry with `True` or `False`")
            return

        # Sets the permission to true or false
        from data import SQLServer_config
        if answer == 'true':
            SQLServer_config.everyone_cure(ctx.guild.id, 1)
        else:
            SQLServer_config.everyone_cure(ctx.guild.id, 0)

        await ctx.send("Settings changed.")

    @commands.command(aliases=["EveryoneCurse", "everyoneCurse", "everyonecurse"])
    @commands.has_permissions(administrator=True)
    async def everyone_can_curse(self, ctx, arg):

        if ctx.message.guild is None:
            await ctx.send("You can't use this command in DMs!")
            return

        # Checks for valid input
        answer = arg.lower()

        if answer != 'true' and answer != 'false':
            await ctx.send("Invalid argument. Please retry with `True` or `False`")
            return

        # Sets the permission to true or false
        from data import SQLServer_config
        if answer == 'true':
            SQLServer_config.everyone_curse(ctx.guild.id, 1)
        else:
            SQLServer_config.everyone_curse(ctx.guild.id, 0)

        await ctx.send("Settings changed.")


def setup(client):
    client.add_cog(Admin(client))
