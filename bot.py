import discord
from discord.ext import commands
from secret import BOT_TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!ratio', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # List of keywords to trigger the bot
    keywords = ['macron', 'aigri', 'égri', 'égris', 'ai gri', 'ai gris', ' é gri', 'aigry', 'égry', 'gris']
    if any(word in message.content.lower() for word in keywords):
        # Send a message to the channel (you can change it easily)
        await message.channel.send('ratio + palu')

# Run the bot 
# BOT_TOKEN is in secret.py
bot.run(BOT_TOKEN)

# RUN python bot.py in your terminal to launch the bot