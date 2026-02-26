import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class LegitPanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.legit_count = 53
        self.not_legit_count = 0
        self.voted_users = set()

    @discord.ui.button(label="✅ 53", style=discord.ButtonStyle.success)
    async def legit_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id in self.voted_users:
            await interaction.response.send_message(
                "❌ You already voted.", ephemeral=True
            )
            return

        self.voted_users.add(interaction.user.id)
        self.legit_count += 1
        button.label = f"✅ {self.legit_count}"
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="❌ 0", style=discord.ButtonStyle.danger)
    async def not_legit_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id in self.voted_users:
            await interaction.response.send_message(
                "❌ You already voted.", ephemeral=True
            )
            return

        self.voted_users.add(interaction.user.id)
        self.not_legit_count += 1
        button.label = f"❌ {self.not_legit_count}"
        await interaction.response.edit_message(view=self)

@bot.command()
async def panel(ctx):
    embed = discord.Embed(
        title="⚫ ETHRAN SHOP • LEGIT CHECK ⚫",
        description=(
            "━━━━━━━━━━━━━━━━━━\n\n"
            "**CLICK ON ✅ IF WE ARE LEGIT**\n\n"
            "**CLICK ON ❌ IF WE ARE NOT LEGIT**\n\n"
            "⚠️ **❌ WITHOUT PROOF = BAN** ⚠️\n\n"
            "━━━━━━━━━━━━━━━━━━"
        ),
        color=0x0f0f0f
    )

    embed.set_footer(text="ETHRAN SHOP • Community Voting")

    await ctx.send(embed=embed, view=LegitPanel())

@bot.event
async def on_ready():
    print(f"🔥 Bot is online as {bot.user}")

bot.run(TOKEN)
