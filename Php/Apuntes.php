<?php
echo "Hola \n";

//Variables:  Siempre primero el $

$my_string = "Esto es una cadena de texto";
$my_string ="Cambio de texto";
echo $my_string . "\n";
echo gettype($my_string);

$my_string = 10 ;
echo $my_string . "\t";
echo gettype($my_string) ;

$my_int=10 ;
echo $my_int. "\n";
$my_int= $my_int -1 . "\t";
echo $my_int. "\n";

$my_double = 555;
echo gettype($my_double) ;
echo $my_double. "\n";

$my_boolean = true;
echo gettype($my_boolean . "/n");
echo $my_boolean == 1 . "\n";
$my_boolean = false ;
echo $my_boolean . "\n";
echo "El valor es $my_int y el boolean es $my_boolean";

//Constantes
const MY_CONSTANTE ="Valor constante";
echo MY_CONSTANTE . "\n";

//Lista
$my_array = [$my_string, $my_int];
echo gettype($my_array);
echo $my_array[0] . "\n";
echo $my_array[1] . "\n";
array_push($my_array, $my_double );
print_r($my_array);