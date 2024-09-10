module.exports = async (message) => {
    // Si el mensaje es de un bot, se ignora
    if (message.author.bot) return;
  
    // Si el mensaje no comienza con un guión (-), se ignora
    if (!message.content.startsWith('-')) return;
  
    // Se extraen los argumentos del mensaje (todo después del primer guión)
    const args = message.content.slice(1).split(' ')[0];
  
    // Manejador de comandos de texto
    try {
      // Se intenta cargar el comando correspondiente desde la carpeta "commands"
      const command = require(`../commands/${args}`);
      // Se ejecuta el comando con el mensaje actual
      command.run(message);
    } catch (error) {
      // Si ocurre un error al cargar o ejecutar el comando, se muestra un mensaje en la consola
      console.log(`Ha ocurrido un error al utilizar el comando -${args}:`);
      console.error(error.message);
    }
  };
  