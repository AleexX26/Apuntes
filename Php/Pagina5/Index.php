    <!DOCTYPE html>
    <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1 style="color: Pink;">Rellena tu CV </h1>
            <form action="/Php/pagina4/introducir.php" method="post">
            <fieldset>
                <legend>Rellena tu CV</legend>
                <p>Nombre</p>
                <select name="Nombre" id="Nombre">
                    <option value="Madrid">Madrid</option>
                    <option value="Barcelona">Barcelona</option>
                    <option value="Sevilla">Sevilla</option>
                    <option value="Malaga">Malaga</option>
                </select>
                <p>Fecha de nacimiento</p>
                <p>
                    <input type=number name="dia" id="dia" min="0" max="31" size="50"> 
                    de 
                    <select name="mes" id="mes">
                    <option value="Enero">Enero</option>
                    <option value="Febrero">Febrero</option>
                    <option value="Marzo">Marzo</option>
                    <option value="Abril">Abril</option>
                    </select> 
                    de 
                    <input type=number name="año" id="año" min="1900" max="2023" size="50" step="50"> 
                    <p>Tema de interes</p>
                    <select multiple="mensaje" name="mensaje" id="mensaje" style="width: 250px;" >
                            <option value="Administracion">Administracion</option>x
                            <option value="Analisis">Analisis</option>
                            <option value="Programacion">Programacion</option>
                            <option value="GTA VI">GTA VI</option>
                            <option value="GTA V">GTA V</option>
                            <option value="GTA IV">GTA IV</option>
                            <option value="GTA III">GTA III</option>
                            <option value="GTA II">GTA II</option>
                    </select>
                    <br>
                    <br>
                    <input type="submit" name="enviar">
                </fieldset>
        </body>
    </html>