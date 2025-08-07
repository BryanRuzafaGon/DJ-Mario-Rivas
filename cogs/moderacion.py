from discord.ext import commands
import discord

class Moderacion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} fue expulsado.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} fue baneado.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def limpiar(self, ctx, cantidad: int):
        await ctx.channel.purge(limit=cantidad + 1)
        await ctx.send(f"🧹 {cantidad} mensajes borrados.", delete_after=3)

async def setup(bot):
    await bot.add_cog(Moderacion(bot))