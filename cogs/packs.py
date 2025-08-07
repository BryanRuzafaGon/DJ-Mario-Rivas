from discord.ext import commands

class Packs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="packs")
    async def packs(self, ctx):
        await ctx.send("🎁 Packs por nivel:
- Nivel 5: Pack Básico
- Nivel 10: Pack Intermedio
- Nivel 20: Pack Pro")

async def setup(bot):
    await bot.add_cog(Packs(bot))