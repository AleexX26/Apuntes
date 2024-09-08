# $dia=Read-Host "Dime un dia de la semana"
# if ($dia -eq "lunes") {
#     Write-Host "Es el primer dia de la semana"
# }elseif ($dia -eq "martes") {
#     Write-Host "Es el segundo dia de la semana"
# }elseif ($dia -eq "miercoles") {
#     Write-Host "Es el tercer dia de la semana"
# }elseif ($dia -eq "jueves") {
#     Write-Host "Es el cuarto dia de la semana"
# }elseif ($dia -eq "viernes") {
#     Write-Host "El el quinto dia de la semana"
# }elseif ($dia -eq "sabado") {
#     Write-Host "Es el sexto dia de la semana"
# }elseif ($dia -eq "domingo") {
#     Write-Host "Es el septimo dia de la semana"
# }else {
#     Write-Host "Eres gilipollas"
# }
# $num=Read-Host "Dime un numero entero para dividir"
# $num1=Read-Host "Dime un numero entero para dividir"
# $total=$num%$num1
# if ($total -eq 0) {
#     Write-Host "La division es exacta"
# }else {
#     Write-Host "La division no es exacta"
# }
# $num=Read-Host "Dime un numero entero para dividir"
# $num1=Read-Host "Dime un numero entero para dividir"
# if ($num1 -eq 0) {
#     Write-Host "No se puede dividir entre cero"
# }
# $total=$num%$num1
# if ($total -eq 0) {
#         Write-Host "La division es exacta"
# }else {
#         Write-Host "La division no es exacta"
# }
# $num3=read-host "Dime un numero"
# $num4=read-host "Dime un numero"
# if ($num3 -lt $num4) {
#     write-host "El numero mayor es $num3 y el menor es $num4"
# }elseif ($num3 -eq $num4) {
    # Write-Host "Los numeros son iguales"
# }

# [int]$dia1=Read-Host "Dime un ano"
# $Multiplo=$dia1%4
# $Multiplo100=$dia1%100
# $Multiplo400=$dia1%400
# if ($multiplo -eq 0) {
#     if ($multiplo400 -eq 0) {
#         Write-Host "Es bisiesto"
#     }elseif ($multiplo100 -eq 0) {
#         Write-Host "No es bisiesto"
#     }else {
#         Write-Host "Es bisiesto"
#     }
# }else {
#     Write-Host "No es bisiesto"
# }

# [Float]$peso=Read-Host "dime una capacidad en GB"
# $total2=$peso/1024
# $total3=$peso*1024
# $total4=$peso*1024*1024
# $total5=$peso*1024*1024*1024
# Write-Host "$total2 TB $total3 MB $total4 KB $total5 B"

[string]$forma=Read-Host "Buenas senor pobre que quieres hacer: elige triangulo o circulo"
if ($forma -eq "triangulo" ) {
    [int]$base=Read-Host "dime la base"
    [int]$altura=Read-Host "dime la altura"
    [int]$totalT=$base*$altura/2
    Write-Host "el area del triangulo es $totalT"
}elseif ($forma -eq "circulo") {

    [int]$radio=Read-Host "Dime el radio"
    $totalC=3.14*($radio*$radio)
    Write-Host "el area del circulo es $totalC"
}else {
    Write-Host "no te he preguntado por eso :("
}  
