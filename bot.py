# Pour utiliser ce code vous devez aller sur Discord Developer Portal et créer une application
# Vous devez ensuite créer un bot et récupérer son token
# Vous devez ensuite créer un fichier secret.py et y mettre la ligne suivante: BOT_TOKEN = 'token' 
# Dans le terminal, vous devez installer discord.py avec la commande suivante: pip install discord.py

import discord
from discord.ext import commands
from secret import BOT_TOKEN

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!ratio', intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Liste des mots qui activent le bot
    keywords = ['macron', 'aigri', 'égri', 'égris', 'ai gri', 'ai gris', ' é gri', 'aigry', 'égry', 'gris']
    if any(word in message.content.lower() for word in keywords):
        # Envoie un message dans le channel
        await message.channel.send('ratio + palu')

# Lance le bot
# BOT_TOKEN est dans le fichier secret.py (crée plus haut)
bot.run(BOT_TOKEN)

# Exécuter python bot.py dans le terminal pour lancer le bot