Write-Host "MUY BUENAS BIENVENIDO AL JUEGO QUE TE VA A ROPMPER LA CABEZA"
Write-Host "."
Write-Host "."
Write-Host "."
[string]$b=Read-host "¿Que nivel quieres jugar. Facil, Medio o Dificil?"
$a
$f=12
$m=10
$d=5
$alea=Get-Random -Minimum 0 -Maximum 10
if ($b -eq "Facil") {
    Write-Host "En el nivel facil solo tienes 15 vidas"
    while ($alea -ne $num) {
        [int]$num=Read-Host "introduce el numero del 1 al 10"
        Write-Host "Te quedan $f vidas, recuerda que solo tienes 15 vidas"
        $f=$f-1
        if ($f -lt 0) {
            Write-Host "El juego a terminado, intentalo otra vez"
            if ($f -ne 0) {
                
            }
        }
    }
    Write-Host "Muy bien"
}
if ($b -eq "Medio") {
    Write-Host "En el nivel medio solo tienes 10 vidas"
    while ($alea -ne $num) {
        [int]$num=Read-Host "introduce el numero del 1 al 10"
        Write-Host "Te quedan $m vidas, recuerda que solo tienes 10 vidas"
        $m=$m-1
        if ($m -lt 0) {
            Write-Host "El juego a terminado, intentalo otra vez"
            if ($m -ne 0) {
        }
    }
    Write-Host "Muy bien"
}
}
if ($b -eq "Dificil") {
    Write-Host "En el nivel dificil solo tienes 5 vidas"
    while ($alea -ne $num) {
        [int]$num=Read-Host "introduce el numero del 1 al 10"
        Write-Host "Te quedan $d vidas, recuerda que solo tienes 5 vidas"
        $d=$d-1
        if ($d -lt 0) {
            Write-Host "El juego a terminado, intentalo otra vez"
            if ($d -ne 0) {
        }
    }
    Write-Host "Muy bien"
}
}
if ($b -eq "F") {
    Write-Host "En el nivel facil solo tienes 15 vidas"
    while ($alea -ne $num) {
        [int]$num=Read-Host "introduce el numero del 1 al 10"
        Write-Host "Te quedan $f vidas, recuerda que solo tienes 15 vidas"
        $f=$f-1
        if ($f -lt 0) {
            Write-Host "El juego a terminado, intentalo otra vez"
            if ($f -ne 0) {
                
            }
        }
    }
    Write-Host "Muy bien"
}
if ($b -eq "M") {
    Write-Host "En el nivel medio solo tienes 10 vidas"
    while ($alea -ne $num) {
        [int]$num=Read-Host "introduce el numero del 1 al 10"
        Write-Host "Te quedan $m vidas, recuerda que solo tienes 10 vidas"
        $m=$m-1
        if ($m -lt 0) {
            Write-Host "El juego a terminado, intentalo otra vez"
            if ($m -ne 0) {
        }
    }
    Write-Host "Muy bien"
}
}
if ($b -eq "D") {
    Write-Host "En el nivel dificil solo tienes 5 vidas"
    while ($alea -ne $num) {
        [int]$num=Read-Host "introduce el numero del 1 al 10"
        $d=$d-1
        if ($d -lt 0) {
            Write-Host "El juego a terminado, intentalo otra vez"
            Write-Host "Te quedan $d vidas, recuerda que solo tienes 5 vidas"
            if ($d -ne 0) {
                Write-Host "Muy bien"
        }
    }
}
}