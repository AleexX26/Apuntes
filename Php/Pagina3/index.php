<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Formulario de registro</h1>
    <form action="ejer.php" method="post">
        <input type=text name="nombre" id="nombre" placeholder="Introduce el nombre"required>
        <input type=email name="email" id="email"placeholder="Introduce el email" required>
        <input type=textarea name="mensaje" id="mensaje" placeholder="Introduce elmensaje" required>
        <input type="submit" name="enviar">
    </form>
</body>
</html>