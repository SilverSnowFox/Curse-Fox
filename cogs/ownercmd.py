from discord.ext import commands
import json


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Addserver", "addserver", "addServer"])
    async def add_server(self, ctx, guild_id):
        # Manually adds server
        try:
            with open("./data/admin.json", "r") as f:
                admins = json.load(f)

                # Checks that user is a bot admin
                if ctx.message.author.id in admins:
                    int(guild_id)

                    # Checks that server exists
                    from data import SQLServer_config as sqlsc
                    if not sqlsc.server_exists(guild_id):
                        sqlsc.new_server(guild_id)

                        from data import SQLServer_curses
                        SQLServer_curses.initiate_server(guild_id)

                        await ctx.send("Guild added.")
                    else:
                        await ctx.send("Guild already exists in DB.")
                else:
                    await ctx.send("This is an admin only command.")
        except FileNotFoundError:
            await ctx.send("No admin.json found.")

    @commands.command(aliases=["RemoveServer", "Removeserver", "removeServer"])
    async def remove_server(self, ctx, guild_id):
        # Manually removes server
        try:
            with open("./data/admin.json", "r") as f:
                admins = json.load(f)

                # Checks that the author is a bot admin
                if ctx.message.author.id in admins:
                    int(guild_id)

                    # Checks that server exists
                    from data import SQLServer_config as sqlsc
                    if sqlsc.server_exists(guild_id):
                        sqlsc.delete_server(guild_id)

                        from data import SQLServer_curses
                        SQLServer_curses.delete_server(guild_id)

                        await ctx.send("Guild removed.")
                    else:
                        await ctx.send("Guild doesn't exist in DB.")
                else:
                    await ctx.send("This is an admin only command.")
        except FileNotFoundError:
            await ctx.send("No admin.json found.")

    @commands.command(aliases=["ServerCount", "Servers"])
    async def server_count(self, ctx):
        await ctx.send(f"I'm currently online in {len(self.client.guilds)} servers")


def setup(client):
    client.add_cog(Owner(client))
