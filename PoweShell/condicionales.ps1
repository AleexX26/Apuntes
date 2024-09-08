[int]$edad=read-host "Cuantos anos tienes"
if ($edad -ge 18) {
Write-Host "Bienvenido. El precio de la entrada es de 10 Euros con consumicion"
}
if ($edad -ge 18) {
    Write-Host "Bienvenido. El precio de la entrada es de 10 Euros con consumicion"
}else {
     Write-Host "vete a tu puta casa"
}
[float]$num=Read-Host "Dame un numero"
if ($num -eq 0) {
    Write-Host "El numero es cero"
}

[int]$num1=Read-Host "Dame un numero"
[int]$num2=Read-Host "Dame un numero"

if ($num1 -eq $num2) {
    Write-Host "Muy bien los dos teneis el mismo numero"
}else {
    Write-Host "inntentalo otra vez a ver si coincidis"
}