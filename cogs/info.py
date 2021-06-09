import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["curses", "Curses"])
    async def curses_list(self, ctx):

        if ctx.message.guild is None:
            await ctx.send("You can't use this command in DMs!")
            return

        guild_id = ctx.guild.id

        # Gets a List[tuple] of the curses
        from data import SQLServer_curses
        all_curses = SQLServer_curses.get_all_curses(guild_id)

        guild_name = ctx.message.guild.name

        if all_curses is None:
            await ctx.send(f"No curses exist in {guild_name}.")
            return

        embed = discord.Embed(title=f"{guild_name}'s curses", colour=discord.Colour.dark_purple())

        k = 0
        while k < len(all_curses):
            text = ""
            y = 0
            while y < 10 and (y + k) < len(all_curses):
                text += "¬ {}\n".format(all_curses[k + y][0])
                y += 1
            embed.add_field(name="\u200b", value=text)
            k += 10

        await ctx.message.author.send(embed=embed)
        await ctx.send("Sent you a DM!")

    @commands.command(aliases=["Latency"])
    async def latency(self, ctx):
        await ctx.send(f"Time taken: {round(self.client.latency * 1000)} ms")


def setup(client):
    client.add_cog(Info(client))
