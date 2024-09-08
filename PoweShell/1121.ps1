# $num=0
# while ($num -le 100 ) {
#     Write-Host "saludos"
#     $num++
# }
# $num2=Read-Host "Dime un numero"
# $num1=0
# while ($num1 -lt $num2 ) {
#     Write-Host "$num1"
#     $num1=$num1+1
# }

# while ($h -ne 0) {
#  $h=Read-Host "dime un numero"
# if ($h -eq 0) {
#     Write-Host "El bucle se para"
#     return
# }else {
#     Write-Host "Es mayor que cero"
# }
# }

# $letra1=Read-Host "Dime una palabra"
# while ($letra1 ) {
#     Write-Host "$letra1"
#     $letra1
# }

$1=Read-Host "Dime un numero"
$2=$1%2
$3=$2%2
$4=$3%2
$5=$4%3 
Write-Host "$2 $3 $4 $5"