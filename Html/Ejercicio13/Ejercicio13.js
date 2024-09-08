var numero=("Dime una nota del 1 al 10")
var nota=prompt(numero)
var contador=0;
while(nota!=0){
    contador=contador+1;
    if(nota<=4){
        alert("Suspenso prearate para el siguiente examen, has introduciodo "+ contador +" Numeros de veces" )
        var si_no=prompt("Desea continuar?(si o no)")
        if(si_no=="si"){
            nota=prompt("Dime una nota del 1 al 10")
        }else if(si_no=="no"){
            break;
        }
    }else if(nota<=10){
        alert("Muy bien has aprobado, has introduciodo "+ contador +" Numeros de veces")
        var si_no=prompt("Desea continuar?(si o no)")
        if(si_no=="si"){
            nota=prompt("Dime una nota del 1 al 10")
        }else if(si_no=="no"){
            break;
        }
    }else{
        alert("No es una nota mayor que 10, has introduciodo "+ contador +" Numeros de veces")
        var si_no=prompt("Desea continuar?(si o no)")
        if(si_no=="si"){
            nota=prompt("Dime una nota del 1 al 10")
        }else if(si_no=="no"){
            break;
        }
        
    }
}