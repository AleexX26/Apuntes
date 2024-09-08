# [int]$num=read-host "Dime un numero"
# $cont= 0
# $cont1= 0
#     while ($num -ne 0) {
#         if ($num -gt 0) {
#             $cont=$cont+1
#             Write-Host "$cont positivos"
#         }
#         elseif ($num -ne 0) {
#             $cont1=$cont1+1
#             Write-Host "$cont1 negativos"
#         }
#         else {
#             Write-host "Error"
#         }
#         [int]$num=Read-Host "Sigue intentado"

#     }

while($cont -lt 5){
    [Float]$nota=Read-Host "Dime la nota"
    $acumulado=$acumulado+$nota
    $cont=$cont+1
}
$avg=$acumulado/5
Write-Host "La media es $avg"

# if ($avg -ge 5) {
#     Write-Host"Aprobado"
# }
# else{
#     Write-Host "Suspenso"
# }