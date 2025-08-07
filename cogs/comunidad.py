from discord.ext import commands
from discord import app_commands, Embed
import discord

class Comunidad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_any_role("Admin", "Moderador")
    @commands.command(name="anuncio")
    async def anuncio(self, ctx, *, mensaje):
        embed = Embed(title="📢 Anuncio", description=mensaje, color=0xffd700)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Comunidad(bot))