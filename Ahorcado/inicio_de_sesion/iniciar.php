<?php
// Establecer la conexión a la base de datos (reemplaza con tus propios datos)
$usuario_bd = "root";
$password_bd = "";
$servidor_bd = "localhost";
$basededatos = "crear_cuenta";

// Crear conexión
$conexion = mysqli_connect($servidor_bd, $usuario_bd, $password_bd, $basededatos);

// Verificar la conexión
if (!$conexion) {
    die("La conexión falló: " . mysqli_connect_error());
}

// Obtener los datos del formulario
$usuario_form = $_POST['usuario'];
$password_form = $_POST['password'];

// Consulta SQL para verificar el usuario y la contraseña en la base de datos
$sql = "SELECT * FROM datos WHERE usuario='$usuario_form' AND password='$password_form'";
$resultado = mysqli_query($conexion, $sql);

// Verificar si se encontró un usuario con los datos proporcionados
if (mysqli_num_rows($resultado) > 0) {
    // Usuario autenticado correctamente
    echo "¡Inicio de sesión exitoso!";
    // Aquí podrías redirigir a otra página o realizar alguna acción adicional
} else {
    // Usuario no encontrado o credenciales incorrectas
    echo "Usuario o contraseña incorrectos";
}

mysqli_close($conexion);
?>
