const { ButtonBuilder, ActionRowBuilder, ButtonStyle } = require('discord.js');

const usernameButton = new ButtonBuilder()
    .setCustomId('username')
    .setEmoji('🗒️')
    .setLabel('Mostrar nombre de usuario.')
    .setStyle(ButtonStyle.Primary);

const avatarButton = new ButtonBuilder()
    .setCustomId('avatar')
    .setEmoji('🖼️')
    .setLabel('Mostrar avatar de usuario.')
    .setStyle(ButtonStyle.Secondary);

module.exports = {
    description: 'Envía dos botones, uno envía el nombre del usuario y el otro la imagen.',
    run: async (message) => {
        const actionRow = new ActionRowBuilder().addComponents(usernameButton, avatarButton);
        const reply = await message.reply({ components: [actionRow] });

        // Crear un recolector de componentes
        const filter = (interaction) => interaction.user.id === message.author.id && interaction.message.id === reply.id;
        const collector = message.channel.createMessageComponentCollector({
            filter, time: 60 * 1000
        });

        // Cuando el recolector recoja un componente
        collector.on('collect', async (interaction) => {
            if (interaction.customId === 'username') {
                await interaction.update({
                    content: `Tu nombre es **${message.author.username}**`,
                    components: []
                });
            } else if (interaction.customId === 'avatar') {
                const avatar = message.author.displayAvatarURL({ size: 512 });

                await interaction.update({
                    content: 'Tu imagen de perfil es:',
                    files: [avatar],
                    components: []
                });
            }
        });

        // Cuando termine el recolector
        collector.on('end', async () => {
            await reply.edit({ components: [] }).catch(console.error);
        });
    }
};
