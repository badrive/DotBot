import discord
from discord.ext import commands

class HelloCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="hello", description="say Hello!")
    async def hello_cog(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"hello {interaction.user.mention}")


async def setup(bot: commands.Bot):
    await bot.add_cog(HelloCog(bot))