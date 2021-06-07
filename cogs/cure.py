import discord
from discord.ext import commands


class Cure(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Cure"])
    async def cure(self, ctx, member=discord.Member):
        try:
            guild_id = ctx.guild.id
            user_id = member.id

            from functions import SQLServer_config
            from functions import SQLUser_cursed
            everyone_can = SQLServer_config.can_everyone_cure(guild_id)
            cursed_user = SQLUser_cursed.user_is_cursed(guild_id, user_id)

            if not cursed_user:
                await ctx.send("Can't cure that who is not cursed.")
            elif everyone_can or ctx.message.author.server_permissions.administrator:
                SQLUser_cursed.cure_user(guild_id, user_id)
                await ctx.send(f"{member.mention} is cured!")
            await ctx.send("The cursed cannot cure each other!")

        except commands.MissingRequiredArgument:
            await ctx.send("Please mention a user to cure.")

    @commands.command(aliases=["Masscure", "masscure"])
    @commands.has_permissions(administrator=True)
    async def mass_cure(self, ctx):
        try:
            from functions import SQLUser_cursed
            SQLUser_cursed.cure_server(ctx.guild.id)

        except commands.MissingPermissions:
            await ctx.send("This is an admin only command.")

    @commands.command(alises=["EveryoneCure", "everyoneCure", "everyonecure"])
    @commands.has_permissions(administrator=True)
    async def everyone_can_cure(self, ctx, arg):
        try:
            # Checks for valid input
            arg.lower()
            if arg != 'true' and arg != 'false':
                await ctx.send("Invalid argument. Please retry with `True` or `False`")
                return

            # Sets the permission
            from functions import SQLServer_config
            if arg == 'true':
                SQLServer_config.everyone_cure(ctx.guild.id, 1)
            else:
                SQLServer_config.everyone_cure(ctx.guild.id, 0)

            await ctx.send("Settings changed.")

        except commands.MissingPermissions:
            await ctx.send("This is an admin only command.")
        except commands.MissingRequiredArgument:
            await ctx.send("Missing arguments.")


def setup(client):
    client.add_cog(Cure(client))
