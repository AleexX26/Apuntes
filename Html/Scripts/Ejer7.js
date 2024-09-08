alert("Hello World!");
var dato = parseFloat(prompt("Ingrese un dato"));
var dato2 = parseFloat(prompt("Ingrese un dato"));
var simbolo = prompt("Ingrese un simbolo");
var resultado;

switch (simbolo) {
    case "+":
        resultado = dato + dato2;
        break;
    case "-":
        resultado = dato - dato2;
        break;
    case "*":
        resultado = dato * dato2;
        break;
    case "/":
        resultado = dato / dato2;
        break;
    case "%":
        resultado = dato % dato2;
        break;
    case "^":
        resultado = Math.pow(dato, dato2);
        break;
    default:
        alert("Operación no válida");
}

alert("Resultado: " + resultado);