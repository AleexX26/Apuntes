function click(){
    var elemento = document.getElementById('bloque1');
    var nuevaPosicionX = Math.random() * (window.innerWidth - 100); // Ajusta según el tamaño de tu elemento
    var nuevaPosicionY = Math.random() * (window.innerHeight - 100); // Ajusta según el tamaño de tu elemento
    elemento.style.transform = 'translate(' + nuevaPosicionX + 'px, ' + nuevaPosicionY + 'px)';
}