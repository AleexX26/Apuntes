const { GuildMember } = require("discord.js");
const { createCanvas, registerFont, loadImage } = require("canvas");

const defaultIcon =
    "https://logodownload.org/wp-content/uploads/2017/11/discord-logo-1-1.png";
const backgroundPath = "./assets/images/background.png";
const fontPath = "./assets/fonts/Quicksand.ttf";
const subtitle = "Bienvenid@ al servidor!";
const avatarRadius = 150;

registerFont(fontPath, { family: "Quicksand" });

/**
 * Retorna un buffer de una imagen de bienvenida
 * @param {GuildMember} member
 */

module.exports = async (member) => {
    // Datos del miembro
    const username = member.user.username;
    const avatar =
        member.user.avatarURL({ size: 256, extension: "png" }) || defaultIcon;

    // Crear lienzo
    const canvas = createCanvas(1200, 600);
    const ctx = canvas.getContext("2d");

    // Dibujar fondo

    // aplicar sombreado
    ctx.shadowColor = "rgba(0,0,0,0.5)";
    ctx.shadowBlur = 15;
    ctx.shadowOffsetX = 5;
    ctx.shadowOffsetY = 5;

    const margin = 20;
    const background = await loadImage(backgroundPath);

    ctx.drawImage(
        background,
        margin,
        margin,
        canvas.width - margin * 2,
        canvas.height - margin * 2
    );
    // dibujar nombre de usuario
    ctx.font = "80px Quicksand";
    ctx.fillStyle = "white";

    ctx.shadowColor = "rgba(0, 0, 0, 0.8)";
    ctx.shadowBlur = 5;

    const usernameMetrics = ctx.measureText(username);

    ctx.fillText(
        username,
        canvas.width / 2 - usernameMetrics.width / 2,
        (canvas.height * 3) / 4
    );

    const avatarImage = await loadImage(avatar);
    // dibujar subtítulo
    ctx.font = "50px Quicksand";
    ctx.fillStyle = "white";

    const subtitleMetrics = ctx.measureText(subtitle);

    ctx.fillText(
        subtitle,
        canvas.width / 2 - subtitleMetrics.width / 2,
        (canvas.height * 3) / 4 + 60
    );
    // dibujar avatar del usuario
    ctx.shadowColor = "rgba(0, 0, 0, 0.4)";
    ctx.shadowBlur = 15;

    // borde
    ctx.beginPath();
    ctx.arc(canvas.width / 2, canvas.height / 3, avatarRadius, 0, Math.PI * 2);
    ctx.closePath();
    ctx.fill();

    // avatar de usuario
    ctx.shadowColor = "transparent";

    ctx.beginPath();
    ctx.arc(
        canvas.width / 2,
        canvas.height / 3,
        avatarRadius - 5,
        0,
        Math.PI * 2
    );
    ctx.closePath();

    ctx.clip();
    ctx.drawImage(
        avatarImage,
        canvas.width / 2 - (avatarRadius - 5),
        canvas.height / 3 - (avatarRadius - 5),
        avatarRadius * 2,
        avatarRadius * 2
    );
    return canvas.toBuffer();
};
