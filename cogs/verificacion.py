from discord.ext import commands
import discord

class Verificacion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = discord.utils.get(self.bot.get_all_channels(), name="verificación")
        if channel:
            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="Verificarse", style=discord.ButtonStyle.green, custom_id="verify"))
            await channel.send("Pulsa el botón para verificarte y obtener acceso.", view=view)

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        if interaction.type == discord.InteractionType.component and interaction.data["custom_id"] == "verify":
            role = discord.utils.get(interaction.guild.roles, name="Verificado")
            if role:
                await interaction.user.add_roles(role)
                await interaction.response.send_message("✅ ¡Verificado!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Verificacion(bot))