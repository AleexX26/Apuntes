<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alex</title>
    <link rel="stylesheet" href="Estilo1.css">
</head>
<body>
    <form action="/Php/Alex/Introducir.php" method="post">
        <div class="padre">
            <p class="cuenta"> CREAR CUENTA</p>
            <br/>
            <p class="usuario"> Usuario</p>
            <input type="text" id="Nombre" name="Nombre" placeholder="Usuario" required style="text-align: center;">
            <p class="usuario">Correo electronico</p>
            <input type="email" id="Correo" name="Correo" placeholder="Correo electronico" required style="text-align: center;">
            <p class="usuario"> Contraseña</p>
            <input type="password" id="Contrasena" name="Contraseña" placeholder="Contraseña" required style="text-align: center;">
            <a href="Index.html"><input type="submit" value="Entrar" class="entrar"></a>
        </div>
    </form>
</body>
</html>