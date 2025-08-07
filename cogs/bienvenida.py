from discord.ext import commands

class Bienvenida(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        canal = next((c for c in member.guild.text_channels if c.name == "bienvenida"), None)
        if canal:
            await canal.send(f"👋 Bienvenido {member.mention} al servidor **{member.guild.name}**!")

async def setup(bot):
    await bot.add_cog(Bienvenida(bot))