import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io
import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener el token de Discord desde el archivo .env
TOKEN = os.getenv("DISCORD_TOKEN_BIENVENIDAS")

# IDs de los canales
WELCOME_CHANNEL_ID = 1282498017458524200  # Reemplaza con el ID del canal de bienvenida

# Intents para manejar los eventos de miembros
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Cargar fuentes y fondo
FONT_PATH = "./Img/Sunflower.otf"  # Reemplaza con la ruta a tu archivo de fuente .otf (si se usa)
BACKGROUND_PATH = "./Img/background.png"  # Reemplaza con la ruta a la imagen de fondo

# Evento cuando un miembro se une al servidor
@bot.event
async def on_member_join(member):
    try:
        await send_welcome_image(member)
    except Exception as e:
        print(f"Error al enviar la imagen de bienvenida: {e}")

# Función para generar la imagen de bienvenida
async def send_welcome_image(member):
    # Abrir la imagen de fondo personalizada
    background = Image.open(BACKGROUND_PATH).convert("RGBA")
    draw = ImageDraw.Draw(background)

    # Cargar el avatar del usuario
    avatar_bytes = io.BytesIO(await member.display_avatar.read())  # Descargar el avatar del usuario
    avatar = Image.open(avatar_bytes).resize((800, 800)).convert("RGBA")  # Redimensionar el avatar a 800x800 y convertir a RGBA

    # Pegar el avatar en el centro de la imagen de fondo
    avatar_position = (
        int(background.width / 2 - avatar.width / 2),
        int(background.height / 2 - avatar.height / 2)
    )
    background.paste(avatar, avatar_position, avatar)  # Pegar el avatar con transparencia

    # (Opcional) Añadir texto si es necesario
    # if os.path.exists(FONT_PATH):
    #     font = ImageFont.truetype(FONT_PATH, size=50)
    #     text = f"Bienvenido {member.display_name}"
    #     text_position = (10, 10)  # Cambia la posición según sea necesario
    #     draw.text(text_position, text, font=font, fill="white")

    # Guardar la imagen en un buffer
    buffer = io.BytesIO()
    background.save(buffer, format="PNG")
    buffer.seek(0)

    # Obtener el canal de bienvenida
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    # Enviar la imagen junto con el mensaje de bienvenida
    if channel:
        await channel.send(
            content=f"¡Bienvenido @{member.display_name} al servidor!", 
            file=discord.File(fp=buffer, filename="bienvenida.png")
        )
    else:
        print(f"Error: No se encontró el canal con ID {WELCOME_CHANNEL_ID}")

# Corre el bot
bot.run(TOKEN)
