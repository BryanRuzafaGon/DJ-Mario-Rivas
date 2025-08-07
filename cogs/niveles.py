from discord.ext import commands
import sqlite3

class Niveles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect("nivel_data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS niveles (user_id INTEGER, xp INTEGER)")
        self.conn.commit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        user_id = message.author.id
        self.cursor.execute("SELECT xp FROM niveles WHERE user_id=?", (user_id,))
        result = self.cursor.fetchone()
        if result:
            xp = result[0] + 10
            self.cursor.execute("UPDATE niveles SET xp=? WHERE user_id=?", (xp, user_id))
        else:
            self.cursor.execute("INSERT INTO niveles (user_id, xp) VALUES (?, ?)", (user_id, 10))
        self.conn.commit()

    @commands.command()
    async def nivel(self, ctx):
        user_id = ctx.author.id
        self.cursor.execute("SELECT xp FROM niveles WHERE user_id=?", (user_id,))
        result = self.cursor.fetchone()
        if result:
            await ctx.send(f"📈 {ctx.author.mention} tienes {result[0]} XP.")
        else:
            await ctx.send("No tienes XP aún. ¡Empieza a participar!")

async def setup(bot):
    await bot.add_cog(Niveles(bot))