<?php 
$usuario = "root";
$password= "";
$servidor= "localhost";
$basededatos="for3";
$conexion=mysqli_connect($servidor, $usuario, "") or die ("error connecting to");
$db = mysqli_select_db($conexion, $basededatos) or die ("Error");
$Provincia= $_POST['Provincia'];
$dia= $_POST['dia'];
$mes= $_POST['mes'];
$año= $_POST['año'];
$mensaje= $_POST['mensaje'];
$sql="insert into cv values ('$Provincia','$dia','$mes','$año','$mensaje')";

$ejecutar=mysqli_query($conexion, $sql);

if (!$ejecutar){
    echo"hubo algun error";
}else{
    echo "datos guardados <br> <a href='index.php'> volver</a>";
}
?>