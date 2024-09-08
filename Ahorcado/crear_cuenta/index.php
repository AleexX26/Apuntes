<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crear Cuenta</title>
    <link rel="stylesheet" href="estilo.css">
</head>

<body>
    <div class="padre">
        <form method="post" action="/Ahorcado/crear_cuenta/crear.php" >
            <section class="form-register">
            <h4>Formulario Registro</h4>
            <input class="controls" type="text" name="usuario" id="usuario" placeholder="Ingrese su Usuario">
            <input class="controls" type="email" name="correo" id="correo" placeholder="Ingrese su Correo">
            <input class="controls" type="password" name="contrasena" id="contrasena" placeholder="Ingrese su Contraseña">
            <input class="botons" type="submit" value="Registrar">
            <p><a href="/Ahorcado/inicio_de_sesion/index.php">¿Ya tengo Cuenta?</a></p>
            </section>
        </form>
    </div>
</body>

</html>