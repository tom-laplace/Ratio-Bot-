# Utilise l'image Python comme base
FROM python:3.8

# Installe les dépendances requises
RUN pip install discord.py

# Copie le code de l'application dans le conteneur
COPY bot.py /app/bot.py
COPY secret.py /app/secret.py

# Définit /app comme répertoire de travail
WORKDIR /app

# Exécute l'application
CMD ["python", "bot.py"]
