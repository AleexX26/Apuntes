$b=Read-Host "Que quieres hacer 1 crear 2 borar "
$i=0
if ($b -eq "si")
{while($i -lt $b){
    $i++
    Net user Profesor$I pass$1 /logonpasswordchg:yes /time:lunes-viernes,8am-1pm,3pm-6pm /add
}
}elseif($i -eq "no"){
    while($i -lt $b){
        $i++
        Net user Profesor$I /delete
    }
}
