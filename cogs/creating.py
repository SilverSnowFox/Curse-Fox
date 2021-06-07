from functions import SQLServer_curses
from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Create", "create"])
    @commands.has_permissions(administrator=True)
    async def delete_curse(self, ctx, arg):
        try:
            # Gets guild ID
            guild_id = ctx.guild.id
            # Checks that Curse exists before deleting
            if SQLServer_curses.curse_exists(guild_id, arg):
                SQLServer_curses.delete_curse(guild_id, arg)
                await ctx.send("Curse deleted.")
                return
            await ctx.send("Curse doesn't exist.")

        except commands.MissingRequiredArgument:
            await ctx.send("Missing arguments.")
        except commands.MissingPermissions:
            await ctx.send("This is an admin only command.")

    @commands.command(aliases=["delete", "Delete"])
    @commands.has_permissions(administrator=True)
    async def create_curse(self, ctx, arg):
        try:
            # Gets guild ID
            guild_id = ctx.guild.id

            # Limit curses to at most 20 characters
            if len(arg) > 20:
                await ctx.send("Please limit the curse to at most 20 characters.")
                return

            # Makes sure that the characters are allowed
            import json
            with open('../data/allowed_characters.json', "r") as f:
                allowed_char = json.load(f)
                check = True
                for char in arg:
                    if char not in allowed_char:
                        check = False
                        break
            # Checks that curse doesn't exist before creating and that is valid
            exists = not SQLServer_curses.curse_exists(guild_id, arg)
            if check and exists:
                SQLServer_curses.create_curse(guild_id, arg)
                await ctx.send("Curse created.")
                return
            elif exists:
                await ctx.send("Curse already exists")
                return
            await ctx.send("Invalid curse.")

        except FileExistsError:
            await ctx.send("allowed_characters.json doesn't exist.")
        except commands.MissingRequiredArgument:
            await ctx.send("Missing arguments.")
        except commands.MissingPermissions:
            await ctx.send("This is an admin only command.")


def setup(client):
    client.add_cog(Guilds(client))
