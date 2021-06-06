from discord.ext import commands
import json
import SQLServer_config as sqlsc


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Addserver", "addserver", "addServer"])
    async def add_server(self, ctx, guild_id):
        # Manually adds server
        try:
            with open("../data/admin.json", "r") as f:
                admins = json.load(f)
                # Checks that user is a bot admin
                if ctx.message.author.id in admins:
                    int(guild_id)
                    # Checks that server exists
                    if sqlsc.server_exists(guild_id):
                        sqlsc.new_server(guild_id)
                        await ctx.send("Server added.")
                    else:
                        await ctx.send("Invalid guild.")
                else:
                    await ctx.send("This is an admin only command.")
        except FileNotFoundError:
            await ctx.send("No admin.json found.")
        except commands.MissingRequiredArgument:
            await ctx.send("Missing arguments.")

    @commands.command(aliases=["RemoveServer", "Removeserver", "removeServer"])
    async def remove_server(self, ctx, guild_id):
        # Manually removes server
        try:
            with open("../data/admin.json", "r") as f:
                admins = json.load(f)
                # Checks that the author is a bot admin
                if ctx.message.author.id in admins:
                    int(guild_id)
                    # Checks that server exists
                    if sqlsc.server_exists(guild_id):
                        sqlsc.delete_server(guild_id)
                        await ctx.send("Server added.")
                    else:
                        await ctx.send("Invalid guild.")
                else:
                    await ctx.send("This is an admin only command.")
        except FileNotFoundError:
            await ctx.send("No admin.json found.")
        except commands.MissingRequiredArgument:
            await ctx.send("Missing arguments.")


def setup(client):
    client.add_cog(Owner(client))
