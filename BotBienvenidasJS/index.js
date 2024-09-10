require('dotenv').config(); // Cargar variables de entorno desde .env

const { Client, Events } = require('discord.js');
const fs = require("fs");
const path = require("path");

const client = new Client({
    intents: 53608447
});

fs.readdirSync("./events")
.filter((filename) => filename.endsWith(".js"))
.forEach((filename) => {
    try {
        const listener = require(`./events/${filename}`);
        const eventName = path.basename(filename, ".js");
        client.on(eventName, listener);
    } catch (err) {
        console.log("[err] Ha ocurrido un error al cargar un evento", err);
    }
});

// Usa el token desde las variables de entorno
client.login(process.env.DISCORD_TOKEN).catch(error => console.error('Error al iniciar sesión:', error));
