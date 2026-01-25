import os
import discord
from discord.ext import commands
from flask import Flask, request
import threading
import requests

TOKEN = os.getenv("TOKEN")
ESP32_URL = os.getenv("ESP32_URL")  # URL publique de l'ESP32

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Serveur Flask pour communiquer avec l'ESP32
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot ESP32 en ligne"

@app.route("/led", methods=["GET"])
def led_control():
    state = request.args.get("state")
    print(f"ESP32 demande LED {state}")
    return f"LED set to {state}", 200

# Commande Discord pour tester le bot
@bot.command()
async def test(ctx):
    await ctx.send("Connecté")

# Commande Discord pour allumer/éteindre la LED via ESP32
@bot.command()
async def led(ctx, arg):
    try:
        response = requests.get(f"{ESP32_URL}/led?state={arg}")
        await ctx.send(f"ESP32 : {response.text}")
    except:
        await ctx.send("Erreur : impossible de contacter l'ESP32")

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")

def run_flask():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_flask).start()
bot.run(TTOKEN)
