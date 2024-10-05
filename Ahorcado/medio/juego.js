// Variables para el juego
let palabrita;
let cant_errores = 0; // Contador de errores
let cant_aciertos = 0; // Contador de aciertos

// Lista de palabras para adivinar
const palabras = [
    'Reyes', 'Burra', 'Aguinaldo', 'Campana', 'Nieve', 'Rudolph', 'Vela', 'Pino'
];

// Obtener referencias a elementos del DOM
const btn = document.getElementById('jugar');
const btnAyuda = document.getElementById('ayuda');
const imagen = document.getElementById('imagen');
const btn_letras = document.querySelectorAll("#letras button");

// Evento para iniciar el juego al hacer clic en el botón 'jugar'
btn.addEventListener('click', iniciar);

// Función para iniciar el juego
function iniciar(event) {
    reiniciarJuego(); // Reiniciar toda la información del juego

    const parrafo = document.getElementById('palabra_a_adivinar');
    parrafo.innerHTML = ''; // Limpiar el contenido del párrafo

    const cant_palabras = palabras.length;
    const valor_al_azar = obtener_random(0, cant_palabras);

    // Seleccionar una palabra aleatoria
    palabrita = palabras[valor_al_azar];
    console.log(palabrita);
    const cant_letras = palabrita.length;

    // Habilitar los botones de letras
    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = false;
    }

    // Crear espacios para las letras de la palabra a adivinar
    for (let i = 0; i < cant_letras; i++) {
        const span = document.createElement('span');
        parrafo.appendChild(span);
    }
}

// Evento para manejar el clic en un botón de letra
for (let i = 0; i < btn_letras.length; i++) {
    btn_letras[i].addEventListener('click', click_letras);
}

// Función para manejar el clic en un botón de letra
function click_letras(event) {
    // Obtener las letras a adivinar y el botón presionado
    const spans = document.querySelectorAll('#palabra_a_adivinar span');
    const button = event.target;
    button.disabled = true;

    // Obtener la letra y la palabra a adivinar
    const letra = button.innerHTML.toLowerCase();
    const palabra = palabrita.toLowerCase();

    // Verificar si la letra está en la palabra a adivinar
    let acerto = false;
    for (let i = 0; i < palabra.length; i++) {
        if (letra === palabra[i]) {
            spans[i].innerHTML = letra;
            cant_aciertos++;
            acerto = true;
        }
    }

    // Manejar errores y aciertos
    if (!acerto) {
        cant_errores++;
        const source = `img/img${cant_errores}.png`;
        imagen.src = source;

        // Agregar clases de error y vibración al botón
        button.classList.add('error', 'vibrate');
    }

    // Verificar si se ha perdido o ganado el juego
    if (cant_errores === 7) {
        document.getElementById('resultado').innerHTML = "Perdiste, la palabra era " + palabrita;
        game_over();
    } else if (cant_aciertos === palabrita.length) {
        document.getElementById('resultado').innerHTML = "GANASTE!! WIIIIII";
        game_over();
    }
    console.log("La letra " + letra + " en la palabra " + palabra + " ¿existe?: " + acerto);
}

// Evento para mostrar una pista al hacer clic en el botón 'ayuda'
btnAyuda.addEventListener('click', mostrarAyuda);

// Función para mostrar una pista basada en la palabra actual
function mostrarAyuda() {
    const parrafoAyuda = document.getElementById('ayuda-texto');
    
    const pista = obtenerPista(palabrita); // Obtener pista para la palabra actual
    
    parrafoAyuda.innerHTML = 'Pista: ' + pista; // Mostrar la pista en el párrafo de ayuda
}

// Función para obtener una pista basada en la palabra
function obtenerPista(palabra) {
    const pistas = {
        'Reyes': 'Tres hombres de Oriente que visitaron a Jesús el niño.',
        'Burra': 'Animal que lleva a los Reyes Magos en su viaje a Belén.',
        'Aguinaldo': 'Regalo económico que se da en Navidad.',
        'Campana': 'Instrumento musical que se usa para anunciar la llegada de los Reyes Magos.',
        'Nieve': 'Cristales de hielo que caen del cielo en invierno.',
        'Rudolph': 'El reno de nariz roja que guía a los Reyes Magos en su viaje.',
        'Vela': 'Objeto que se usa para dar luz en Navidad.',
        'Pino': 'Árbol que se decora en Navidad.'
    };

    return pistas[palabra] || 'No hay pista disponible para esta palabra.';
}

// Función para finalizar el juego
function game_over() {
    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = true;
    }

    btn.disabled = false;
}

// Función para reiniciar el juego
function reiniciarJuego() {
    cant_errores = 0;
    cant_aciertos = 0;
    imagen.src = 'img/img0.png';
    document.getElementById('resultado').innerHTML = '';

    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = false;
        btn_letras[i].classList.remove('error', 'vibrate');
    }
    resetearPista(); // Limpiar la pista al reiniciar
}

// Función para limpiar la pista
function resetearPista() {
    const parrafoAyuda = document.getElementById('ayuda-texto');
    parrafoAyuda.innerHTML = ''; // Limpiar la pista
}

// Función para obtener un número aleatorio entre un rango dado
function obtener_random(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}
