from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("Missing arguments.")

        if isinstance(error, commands.errors.MissingPermissions):
            await ctx.send("You can't do this!")


def setup(client):
    client.add_cog(Errors(client))
