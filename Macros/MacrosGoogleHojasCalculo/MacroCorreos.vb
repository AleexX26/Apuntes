
// Esto es una macro en Google Hojas de Calculo, para poder enviar masivamente correos con sus archivos necesarios.

// CAMBIAR LA PALABRA Readme POR EL NOMBRE DE LA HOJA QUE QUIERES QUE FUNCIONE EL SCRIPT, MI RECOMENDACION ES DEJARLO EN Readme.

function enviarCorreosConPDFs() {
  // Obtener la hoja "Readme"
  var hojaReadme = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Readme");

  // Verificar si la hoja "Readme" existe
  if (!hojaReadme) {
    Logger.log("La hoja 'Readme' no existe. Verifica el nombre.");
    return; // Si no existe, termina la ejecución del script
  }

// ---------------> MIRAR QUE TODO ESTE CORRECTO CON LAS CELDAS DE LA HOJA DE CALCULO <-------------

  // Obtener el valor del ID de la carpeta desde la hoja "Readme" (celda D5)
  var folderId = hojaReadme.getRange("D5").getValue(); // Celda D5 tiene el ID de la carpeta
  
  // Obtener el asunto del mensaje desde la hoja "Readme" (celda E5)
  var asuntoBase = hojaReadme.getRange("E5").getValue(); // Celda E5 tiene el asunto del mensaje

  // Obtener el cuerpo del mensaje desde la hoja "Readme" (celda F5)
  var mensajeBase = hojaReadme.getRange("F5").getValue(); // Celda F5 tiene el cuerpo del mensaje

  // Obtener el nombre de la hoja que contiene los datos de correo y nombre desde la celda H5
  var nombreHojaDatos = hojaReadme.getRange("H5").getValue(); // Celda H5 tiene el nombre de la hoja con los datos

  // Verificar si el nombre de la hoja de datos no está vacío
  if (!nombreHojaDatos) {
    Logger.log("El nombre de la hoja de datos no se encuentra en H5.");
    return; // Si no hay nombre de hoja, termina la ejecución
  }

  // Obtener la hoja con los datos de nombres y correos
  var hojaDatos = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(nombreHojaDatos);

  // Verificar si la hoja de datos existe
  if (!hojaDatos) {
    Logger.log("La hoja '" + nombreHojaDatos + "' no existe. Verifica el nombre.");
    return; // Si no existe, termina la ejecución del script
  }

  // Obtener los datos de la hoja de nombres y correos
  var data = hojaDatos.getDataRange().getValues(); // Lee todos los datos de la hoja con el nombre obtenido de H5
  
  // Acceder a la carpeta en Google Drive
  var folder = DriveApp.getFolderById(folderId);
  
  // Iterar por cada fila de la hoja de datos
  for (var i = 1; i < data.length; i++) { // Comienza en la fila 1 (asumiendo que la fila 0 tiene los encabezados)
    var nombrePDF = data[i][1]; // Columna B (índice 1) tiene los nombres de los PDFs
    var correo = data[i][2];    // Columna C (índice 2) tiene los correos electrónicos
    
    // Verificar que el correo no esté vacío y que sea válido
    if (correo && correo.indexOf("@") > -1) {
      
      // Buscar el archivo PDF en Google Drive
      var archivos = folder.getFilesByName(nombrePDF + '.pdf');
      
      if (archivos.hasNext()) {
        var archivo = archivos.next();
        
        // Crear el cuerpo del mensaje
        var asunto = asuntoBase + ": " + nombrePDF; // Combina el asunto base con el nombre del archivo PDF
        var mensaje = mensajeBase + "\n\nSaludos."; // Añade el cuerpo del mensaje desde F5
        
        // Enviar el correo con el archivo adjunto
        MailApp.sendEmail({
          to: correo,
          subject: asunto,
          body: mensaje,
          attachments: [archivo]
        });
        
        Logger.log("Correo enviado a: " + correo + " );
      } else {
        Logger.log("No se encontró el archivo PDF para " + nombrePDF);
      }
    } else {
      Logger.log("Correo no válido o vacío para la fila " + (i+1));
    }
  }
}
