<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inicio de Sesión</title>
    <link rel="stylesheet" href="estilo.css">
</head>

<body>
    <div class="padre">
        <form method="post" action="/Ahorcado/inicio_de_sesion/login.php" >
            <section class="form-register">
            <h4>Inicio de sesion</h4>
            <input class="controls" type="text" name="credencial" id="credencial" placeholder="Ingrese su Usuario o Correo" required>
            <input class="controls" type="password" name="contrasena" id="contrasena" placeholder="Ingrese su Contraseña" required>
            

            <input class="botons" type="submit" value="Iniciar Sesion">
            <!-- <a class="boton" href="/Ahorcado/main/main.html"> <button class="botons"> Entrar</button> </a> -->
            
            <p><a href="/Ahorcado/crear_cuenta/index.php">No tengo Cuenta</a></p>
            </section>
        </form>
    </div>
</body>

</html>