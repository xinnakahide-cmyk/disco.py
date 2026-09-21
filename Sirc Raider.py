import discord
from discord import app_commands
import asyncio

TOKEN = "MTUzNDM4NjkzNTY4MDczMzIwNA.Gx8gnr.OtcqxQiqQY0bEgBuD33iBZOvAHUzF4vw8i5TFY"

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("RAID MONA TANG INAMO  ")

client = MyClient()

@client.tree.command(name="raid")
@app_commands.describe(
    message="Raid Channel Message",
    amount="Number of times to send the message"
)
async def raid(interaction: discord.Interaction, message: str, amount: int):
    if amount < 1:
        await interaction.response.send_message(" TANGA KABA?", ephemeral=True)
        return

    await interaction.response.send_message("TANGA KABA?", ephemeral=True)
    await asyncio.sleep(0.1)

    sent = 0
    while sent < amount:
        try:
            sent += 1
            await interaction.followup.send(message)  
            
            await asyncio.sleep(0.1)
        except Exception as e:
            await interaction.followup.send(f" # TANG INA NYOOOOOOOO ")
            break

client.run(TOKEN)
6879995