<?php 
$usuario = "root";
$password= "";
$servidor= "localhost";
$basededatos="for2";
$conexion=mysqli_connect($servidor, $usuario, "") or die ("error connecting to");
$db = mysqli_select_db($conexion, $basededatos) or die ("Error");
$nombre= $_POST['nombre'];
$email= $_POST['email'];
$mensaje= $_POST['mensaje'];
$sql="insert into datos values ('$nombre','$email','$mensaje')";
$ejecutar=mysqli_query($conexion, $sql);

if (!$ejecutar){
    echo"hubo algun error";
}else{
    echo "datos guardados <br> <a href='index.php'> volver</a>";
}
?>