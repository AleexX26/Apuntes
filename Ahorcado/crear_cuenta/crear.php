<?php 
$usuario = "root";
$password= "";
$servidor= "localhost";
$basededatos="crear_cuenta";
$conexion=mysqli_connect($servidor, $usuario, "") or die ("error connecting to");
$db = mysqli_select_db($conexion, $basededatos) or die ("Error");
$usuario= $_POST['usuario'];
$correo= $_POST['correo'];
$contrasena= $_POST['contrasena'];
$sql="INSERT into datos VALUES ('$usuario','$correo','$contrasena')";
$ejecutar=mysqli_query($conexion, $sql);

if (!$ejecutar) {
    echo "hubo algún error";
} else {
    echo '<script>alert("Inicio de sesión exitoso"); window.location = "/Ahorcado/inicio_de_sesion/index.php";</script>';
}
?>