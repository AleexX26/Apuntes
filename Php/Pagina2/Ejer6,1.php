<?php
$usuario="root";
$password="";
$servidor="localhost";
$basededatos="for1";
$conexion = mysqli_connect($servidor,$usuario,"") or die ("Error con el servidor de la base de datos");
$db = mysqli_select_db($conexion,$basededatos) or die ("error de conexion al conectarte con la base de datos");
$nombre = $_POST['nombre'];
$edad= $_POST['edad'];
$sql= "INSERT INTO datos2 VALUES('$nombre')";
$sql= "INSERT INTO datos2 VALUES('$edad')";
$ejecutar= mysqli_query($conexion,$sql);

if (!$ejecutar){
    echo"hubo algun error";
}else{
    echo "datos guardados <br> <a href='Ejer6.php'> volver</a>";
}
?>