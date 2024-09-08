<?php 
$usuario = "root";
$password= "";
$servidor= "localhost";
$basededatos="alex";
$conexion=mysqli_connect($servidor, $usuario, "") or die ("error connecting to");
$db = mysqli_select_db($conexion, $basededatos) or die ("Error");
$Nombre= $_POST['Nombre'];
$Correo= $_POST['Correo'];
$Contraseña= $_POST['Contraseña'];
$sql="insert into datos values ('$Nombre','$Correo','$Contraseña')";
$ejecutar=mysqli_query($conexion, $sql);

if (!$ejecutar){
    echo"hubo algun error";
}else{
    echo "datos guardados <br> <a href='index.php'> volver</a>";
}
?>