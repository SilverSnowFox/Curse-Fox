import discord
from discord.ext import commands


class Cure(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Cure"])
    async def cure(self, ctx, member: discord.Member):

        if ctx.message.guild is None:
            await ctx.send("You can't use this command in DMs!")
            return

        guild_id = ctx.guild.id
        user_id = member.id

        from data import SQLServer_config
        everyone_can = SQLServer_config.can_everyone_cure(guild_id)

        from data import SQLUser_cursed
        cursed_user = SQLUser_cursed.user_is_cursed(guild_id, user_id)

        if not cursed_user:
            await ctx.send("Can't cure that who is not cursed.")
            return
        elif everyone_can or ctx.message.author.guild_permissions.administrator:
            SQLUser_cursed.cure_user(guild_id, user_id)
            await ctx.send(f"{member.mention} is cured!")
            return
        elif user_id == ctx.message.author.id:
            await ctx.send("You can't cure yourself!")
            return
        await ctx.send("The cursed cannot cure another!")

    @commands.command(aliases=["Masscure", "masscure"])
    @commands.has_permissions(administrator=True)
    async def mass_cure(self, ctx):

        if ctx.message.guild is None:
            await ctx.send("You can't use this command in DMs!")
            return

        from data import SQLUser_cursed
        SQLUser_cursed.cure_server(ctx.guild.id)
        await ctx.send("Everyone has been cured!")

    @commands.command(alises=["EveryoneCure", "everyoneCure", "everyonecure"])
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


def setup(client):
    client.add_cog(Cure(client))
