
import discord
from discord.ext import commands
from discord import app_commands

class Panel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="panel", description="Ouvrir le panel de configuration")
    async def panel(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Panel de configuration",
                              description="Configurer le bot via les boutons")
        view = PanelView()
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

class PanelView(discord.ui.View):
    @discord.ui.button(label="Logs", style=discord.ButtonStyle.blurple)
    async def logs(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Configuration des logs.", ephemeral=True)

    @discord.ui.button(label="Tickets", style=discord.ButtonStyle.green)
    async def tickets(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Configuration des tickets.", ephemeral=True)

    @discord.ui.button(label="Auto Role", style=discord.ButtonStyle.gray)
    async def autorole(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Configuration auto-role.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Panel(bot))
