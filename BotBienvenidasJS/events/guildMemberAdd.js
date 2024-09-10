const { EmbedBuilder, AttachmentBuilder } = require('discord.js');
const generateImage = require("../utils/canvas/welcomeImage");

const roleId = '1262156970731765831'; // ID del rol que quieres asignar

module.exports = async (member) => {
    const { client } = member;
    const welcomeChannelId = "1225114840620601396";
    const channel = await client.channels.fetch(welcomeChannelId);
    const buffer = await generateImage(member);
    const attachment = new AttachmentBuilder(buffer, {name: "generated-image.png"});

    // Obtén el rol y asígnalo al miembro
    const guild = member.guild;
    try {
        const role = await guild.roles.fetch(roleId);
        if (role) {
            await member.roles.add(role);
            console.log(`Rol ${role.name} asignado a ${member.user.tag}`);
        } else {
            console.log(`Rol con ID ${roleId} no encontrado`);
        }
    } catch (error) {
        console.error('Error al asignar el rol:', error);
    }

    // Crea el embed de bienvenida
    const embed = new EmbedBuilder()
        .setTitle(`¡Bienvenido al servidor!`)
        .setColor("#FF0000")
        .setDescription(
            `¡Bienvenido al servidor! <@${member.user.id}>` 
        )
        .setImage("attachment://generated-image.png");

    channel.send({
        content: ``,
        embeds: [embed],
        files: [attachment],
    });
};
