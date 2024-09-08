<?php
$usuario = "root";
$password = "";
$servidor = "localhost";
$basededatos ="formulario";
$conexion = mysqli_connect($servidor, $usuario, "") or die("Error con el servidor: ");
$db = mysqli_select_db ($conexion, $basededatos) or die("Error con el servidor: ");

$nombre =$_POST['nombre'];
$correo =$_POST['correo'];
$mensaje =$_POST['mensaje'];

echo "Nombre: " . $nombre . "<br/>";
echo "Correo: " . $correo . "<br/>";
echo "mensaje: " . $mensaje . "<br/>";
