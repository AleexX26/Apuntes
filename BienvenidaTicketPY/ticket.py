import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.ui import Button, View

# Cargar las variables del archivo .env
load_dotenv()

# Obtener el token desde el archivo .env (usando DISCORD_TOKEN_TICKET)
TOKEN = os.getenv('DISCORD_TOKEN_TICKET')

if TOKEN is None:
    print("Error: el token no fue cargado desde el archivo .env")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

ticket_channel_id = 1282853349280059463  # Reemplaza con el ID de tu canal de tickets
ticket_category_id = 1282848290848772189  # Reemplaza con el ID de tu categoría de tickets
transcript_category_id = 1282506083071692851  # Reemplaza con el ID de tu categoría de transcripts

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    channel = bot.get_channel(ticket_channel_id)
    if channel:
        view = create_ticket_buttons()
        embed = create_ticket_embed()
        await channel.send(embed=embed, view=view)
    else:
        print("No se pudo encontrar el canal de tickets. Verifica el ID del canal.")

def create_ticket_embed():
    embed = discord.Embed(title="Sistema de Tickets",
                          description="Reacciona al emoji correspondiente para crear un ticket:",
                          color=0x00ff00)
    embed.add_field(name="📩 Soporte", value="Reacciona para abrir un ticket de soporte.", inline=False)
    embed.add_field(name="🔨 Bugs y Fallos", value="Reacciona para reportar un bug o fallo.", inline=False)
    embed.add_field(name="⚠️ Reporte", value="Reacciona para reportar a un jugador.", inline=False)
    embed.add_field(name="📢 Apelaciones", value="Reacciona para abrir un ticket de apelación.", inline=False)
    embed.add_field(name="💰 Donaciones", value="Reacciona para donar.", inline=False)
    embed.add_field(name="🌐 CC/RRSS", value="Reacciona para asuntos de CC/RRSS.", inline=False)
    embed.add_field(name="🔫 Ilegales", value="Reacciona para abrir un ticket de temas ilegales.", inline=False)
    embed.add_field(name="⚖️ Legales", value="Reacciona para temas legales.", inline=False)
    embed.add_field(name="💀 CK", value="Reacciona para abrir un ticket de CK.", inline=False)
    embed.add_field(name="📊 Playmaker", value="Reacciona para abrir un ticket de playmaker.", inline=False)
    embed.add_field(name="📬 Solicitud Roles", value="Reacciona para solicitar roles.", inline=False)
    embed.add_field(name="⚖️ Responsable del Staff", value="Reacciona para contactar con un responsable del staff.", inline=False)
    return embed

def create_ticket_buttons():
    view = View()
    buttons = [
        ("Soporte", "ticket_support"),
        ("Bugs y Fallos", "ticket_bugs"),
        ("Reporte", "ticket_report"),
        ("Apelaciones", "ticket_appeals"),
        ("Donaciones", "ticket_donations"),
        ("CC/RRSS", "ticket_cc_rrss"),
        ("Ilegales", "ticket_illegal"),
        ("Legales", "ticket_legal"),
        ("CK", "ticket_ck"),
        ("Playmaker", "ticket_playmaker"),
        ("Solicitud Roles", "ticket_roles"),
        ("Responsable del Staff", "ticket_staff")
    ]
    
    for label, custom_id in buttons:
        button = Button(label=label, style=discord.ButtonStyle.primary, custom_id=custom_id)
        view.add_item(button)
    
    return view

async def handle_ticket(interaction, category):
    guild = interaction.guild
    member = interaction.user

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        member: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    ticket_category = discord.utils.get(guild.categories, id=ticket_category_id)
    if ticket_category:
        try:
            channel = await guild.create_text_channel(f"ticket-{member.name}-{category}", category=ticket_category, overwrites=overwrites)
            
            close_button = Button(label="Cerrar Ticket", style=discord.ButtonStyle.danger, custom_id="close_ticket")
            view = View()
            view.add_item(close_button)
            await channel.send(f"{member.mention}, bienvenid@ a tu ticket de **{category}**. Por favor, describe tu problema.", view=view)

            try:
                await interaction.response.send_message(f"Tu ticket de {category} ha sido creado: {channel.mention}", ephemeral=True)
            except discord.NotFound as e:
                print(f"Error al enviar mensaje de creación de ticket: {e}")
        except discord.Forbidden as e:
            print(f"Error de permisos al crear o enviar mensajes en el canal del ticket: {e}")
            try:
                await interaction.response.send_message("Error al crear el ticket. Verifica los permisos del bot.", ephemeral=True)
            except discord.NotFound as e:
                print(f"Error al enviar mensaje de error: {e}")
        except Exception as e:
            print(f"Error inesperado al manejar el ticket: {e}")
            try:
                await interaction.response.send_message("Ocurrió un error inesperado al crear el ticket.", ephemeral=True)
            except discord.NotFound as e:
                print(f"Error al enviar mensaje de error: {e}")

@bot.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component:
        custom_id = interaction.data['custom_id']
        if custom_id.startswith("ticket_"):
            category = custom_id.split("_", 1)[1]
            try:
                await handle_ticket(interaction, category)
            except discord.NotFound as e:
                print(f"Canal o interacción no encontrada: {e}")
                try:
                    await interaction.response.send_message("Ocurrió un error al procesar la interacción. Verifica que el canal exista y que el bot tenga permisos.", ephemeral=True)
                except discord.NotFound as e:
                    print(f"Error al enviar mensaje de error: {e}")
            except Exception as e:
                print(f"Error inesperado al manejar la interacción: {e}")
                try:
                    await interaction.response.send_message("Ocurrió un error inesperado. Intenta nuevamente más tarde.", ephemeral=True)
                except discord.NotFound as e:
                    print(f"Error al enviar mensaje de error: {e}")
        elif custom_id == "close_ticket":
            channel = interaction.channel
            transcript_category = discord.utils.get(interaction.guild.categories, id=transcript_category_id)
            if transcript_category:
                transcript_channel = discord.utils.get(transcript_category.text_channels)
                if transcript_channel:
                    try:
                        transcript = await create_transcript(channel)
                        await transcript_channel.send(f"Transcript del ticket {channel.name}:\n{transcript}")
                        await channel.delete()
                        try:
                            await interaction.response.send_message(f"El ticket {channel.name} ha sido cerrado y el transcript ha sido guardado.", ephemeral=True)
                        except discord.NotFound as e:
                            print(f"Error al enviar mensaje de cierre de ticket: {e}")
                    except discord.NotFound as e:
                        print(f"Canal no encontrado para el transcript: {e}")
                        try:
                            await interaction.response.send_message("Error al guardar el transcript. Verifica que el canal de transcript exista.", ephemeral=True)
                        except discord.NotFound as e:
                            print(f"Error al enviar mensaje de error: {e}")
                    except discord.Forbidden as e:
                        print(f"Error al enviar el mensaje de transcript: {e}")
                        try:
                            await interaction.response.send_message("Error al guardar el transcript. Verifica los permisos del bot.", ephemeral=True)
                        except discord.NotFound as e:
                            print(f"Error al enviar mensaje de error: {e}")
                    except Exception as e:
                        print(f"Error inesperado al cerrar el ticket: {e}")
                        try:
                            await interaction.response.send_message("Ocurrió un error inesperado al cerrar el ticket.", ephemeral=True)
                        except discord.NotFound as e:
                            print(f"Error al enviar mensaje de error: {e}")
                else:
                    try:
                        await interaction.response.send_message("No se encontró un canal de texto en la categoría de transcripts.", ephemeral=True)
                    except discord.NotFound as e:
                        print(f"Error al enviar mensaje de error: {e}")
            else:
                try:
                    await interaction.response.send_message("No se pudo encontrar la categoría para los transcripts.", ephemeral=True)
                except discord.NotFound as e:
                    print(f"Error al enviar mensaje de error: {e}")

async def create_transcript(channel):
    messages = []
    async for message in channel.history(limit=None):
        messages.append(f"{message.author}: {message.content}")

    transcript = "\n".join(messages)
    return transcript

bot.run(TOKEN)
