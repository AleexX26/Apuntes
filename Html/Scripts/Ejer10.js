function moverElemento() {
    var elemento = document.getElementById('caja1');
    var nuevaPosicionX = Math.random() * (window.innerWidth - 50); // Ajusta según el tamaño de tu elemento
    var nuevaPosicionY = Math.random() * (window.innerHeight - 50); // Ajusta según el tamaño de tu elemento
    elemento.style.transform = 'translate(' + nuevaPosicionX + 'px, ' + nuevaPosicionY + 'px)';
}
function moverElemento1() {
    var elemento = document.getElementById('caja2');
    var nuevaPosicionX = Math.random() * (window.innerWidth - 50); // Ajusta según el tamaño de tu elemento
    var nuevaPosicionY = Math.random() * (window.innerHeight - 50); // Ajusta según el tamaño de tu elemento
    elemento.style.transform = 'translate(' + nuevaPosicionX + 'px, ' + nuevaPosicionY + 'px)';
}
function moverElemento2() {
    var elemento = document.getElementById('hijocaja2');
    var nuevaPosicionX = Math.random() * (window.innerWidth - 50); // Ajusta según el tamaño de tu elemento
    var nuevaPosicionY = Math.random() * (window.innerHeight - 50); // Ajusta según el tamaño de tu elemento
    elemento.style.transform = 'translate(' + nuevaPosicionX + 'px, ' + nuevaPosicionY + 'px)';
}
function moverElemento3() {
    var elemento = document.getElementById('hijocaja3');
    var nuevaPosicionX = Math.random() * (window.innerWidth - 50); // Ajusta según el tamaño de tu elemento
    var nuevaPosicionY = Math.random() * (window.innerHeight - 50); // Ajusta según el tamaño de tu elemento
    elemento.style.transform = 'translate(' + nuevaPosicionX + 'px, ' + nuevaPosicionY + 'px)';
}
function moverElemento4() {
    var elemento = document.getElementById('caja3');
    var zindex = moveBy.zindex(500);
    var left = moveBy.left(3);
    elemento.style.left = 'left(' + left + 'px)';
    // var nuevaPosicionX = Math.random() * (window.innerWidth - 50); // Ajusta según el tamaño de tu elemento
    // var nuevaPosicionY = Math.random() * (window.innerHeight - 50); // Ajusta según el tamaño de tu elemento
    // elemento.style.transform = 'translate(' + nuevaPosicionX + 'px, ' + nuevaPosicionY + 'px)';
}   