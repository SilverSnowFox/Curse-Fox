import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["curses", "Curses"], no_pm=True)
    async def curses_list(self, ctx):
        try:
            guild_id = ctx.guild.id

            # Gets a List[tuple] of the curses
            from functions import SQLServer_curses
            all_curses = SQLServer_curses.get_all_curses(guild_id)

            guild_name = ctx.message.guild.name

            if all_curses is None:
                await ctx.send(f"No curses exist in {guild_name}.")
                return

            k = 0
            while k < len(all_curses):
                ind_page = discord.Embed(title=f"List {guild_name}'s curses",
                                         colour=discord.Colour.dark_purple())
                text = ""
                y = 0
                while y < 10:
                    text.join("¬ " + all_curses[k + y][0] + "\n")
                    y += 1
                ind_page.add_field(name="\u200b", value=text)
                k += 10

                await ctx.message.author.send(embed=ind_page)
            await ctx.send("Sent you a DM!")

        except Exception as e:
            print(e)

    @commands.command(aliases=["Cursed", "cursed"])
    async def cursed_users(self, ctx, arg=None):
        # If arg is none, lists amount of cursed users
        # If arg == all/All, lists all of the cursed users in an embed
        # If arg is a mention, return if user is cursed and with what
        # Embed
        pass

    @commands.command(aliases=["Latency"])
    async def latency(self, ctx):
        await ctx.send(f"Time taken: {round(self.client.latency * 1000)} ms")


def setup(client):
    client.add_cog(Info(client))
