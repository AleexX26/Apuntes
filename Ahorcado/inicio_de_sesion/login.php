<?php
$usuario = "root";
$password = "";
$servidor = "localhost";
$basededatos = "crear_cuenta";

$conexion = mysqli_connect($servidor, $usuario, $password, $basededatos) or die("Error connecting to database");

// Verificar la conexión
if ($conexion->connect_error) {
    die("Error en la conexión: " . $conexion->connect_error);
}

// Recuperar datos del formulario
$credencial = $_POST['credencial'];
$contrasena = $_POST['contrasena'];

// Consulta SQL para verificar la existencia del usuario o correo
$sql = "SELECT * FROM datos WHERE (usuario = '$credencial' OR correo = '$credencial') AND contrasena = '$contrasena'";
$resultado = $conexion->query($sql);

// Verificar si la consulta devuelve algún resultado
if ($resultado->num_rows > 0) {
    // Usuario autenticado correctamente
    header("Location: ../main/main.html");
    exit();
} else {
    // Usuario no autenticado
    // Puedes redirigir al usuario a la página de inicio de sesión con un mensaje de error
    echo "<script>
        alert('Usuario o contraseña incorrectos');
        window.location.href='index.php';
    </script>";;
}

// Cerrar la conexión
$conexion->close();
?>
