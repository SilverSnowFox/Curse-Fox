from discord.ext import commands


class Guilds(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["delete", "Delete"])
    @commands.has_permissions(administrator=True)
    async def delete_curse(self, ctx, arg):
        # Lack of administrator perm already blocks DMs
        # Gets guild ID
        guild_id = ctx.message.guild.id
        # Checks that Curse exists before deleting
        from data import SQLServer_curses
        if SQLServer_curses.curse_exists(guild_id, arg):
            SQLServer_curses.delete_curse(guild_id, arg)
            await ctx.send("Curse deleted.")
            return
        await ctx.send("Curse doesn't exist.")

    @commands.command(aliases=["Create", "create"])
    @commands.has_permissions(administrator=True)
    async def create_curse(self, ctx, arg):
        # Lack of administrator perm already blocks DMs
        try:
            # Gets guild ID
            guild_id = ctx.guild.id

            # Limit curses to at most 20 characters
            if len(arg) >= 20:
                await ctx.send("Please limit the curse to at most 20 characters.")
                return

            # Makes sure that the characters are allowed
            import json
            with open('./data/allowed_characters.json', "r") as f:
                allowed_char = json.load(f)
                check = True
                for char in arg:
                    if char not in allowed_char:
                        check = False
                        break

            # Checks that curse doesn't exist before creating and that is valid
            from data import SQLServer_curses
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
        except commands.errors.UnexpectedQuoteError:
            await ctx.send("Invalid curse.")


def setup(client):
    client.add_cog(Guilds(client))
