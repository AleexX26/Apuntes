// Declaración de variables
let palabrita; // Variable para almacenar la palabra a adivinar
let cant_errores = 0; // Variable para contar la cantidad de errores
let cant_aciertos = 0; // Variable para contar la cantidad de aciertos

// Array que contiene las palabras del juego
const palabras = [
    'Regalo',     /* 0 */
    'Adviento',   /* 1 */
    'Pesebre',    /* 2 */
    'Novena',     /* 3 */
    'Villancico', /* 4 */
    'Cagane',     /* 5 */
    'Pastor',     /* 6 */
    'Angel'       /* 7 */
];

// Obtener referencias a elementos del DOM
const btn = id('jugar'); // Botón de inicio del juego
const imagen = id('imagen'); // Imagen para mostrar errores
const btn_letras = document.querySelectorAll("#letras button"); // Botones de letras

// Evento para iniciar el juego cuando se hace clic en el botón 'jugar'
btn.addEventListener('click', iniciar);

// Función para iniciar el juego
function iniciar(event) {
    // Configuración inicial del juego
    imagen.src = 'img/img0.png'; // Imagen inicial
    btn.disabled = true; // Deshabilitar el botón de inicio
    cant_errores = 0; // Reiniciar el contador de errores
    cant_aciertos = 0; // Reiniciar el contador de aciertos

    const parrafo = id('palabra_a_adivinar'); // Párrafo para mostrar la palabra a adivinar
    parrafo.innerHTML = ''; // Limpiar el contenido del párrafo

    // Obtener una palabra aleatoria del array 'palabras'
    const cant_palabras = palabras.length;
    const valor_al_azar = obtener_random(0, cant_palabras);
    palabrita = palabras[valor_al_azar]; // Asignar la palabra aleatoria a 'palabrita'
    console.log(palabrita); // Mostrar la palabra en la consola

    const cant_letras = palabrita.length; // Obtener la cantidad de letras en la palabra

    // Habilitar los botones de letras
    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = false;
    }

    // Mostrar las casillas para las letras de la palabra a adivinar
    for (let i = 0; i < cant_letras; i++) {
        const span = document.createElement('span'); // Crear un elemento span para cada letra
        parrafo.appendChild(span); // Agregar el span al párrafo
    }
}

// Evento para manejar el clic en un botón de letra
for (let i = 0; i < btn_letras.length; i++) {
    btn_letras[i].addEventListener('click', click_letras);
}

// Función para manejar el clic en un botón de letra
function click_letras(event) {
    const spans = document.querySelectorAll('#palabra_a_adivinar span'); // Obtener los spans de la palabra a adivinar
    const button = event.target; // Botón que ha sido clickeado
    button.disabled = true; // Deshabilitar el botón

    const letra = button.innerHTML.toLowerCase(); // Obtener la letra seleccionada
    const palabra = palabrita.toLowerCase(); // Convertir la palabra a minúsculas

    let acerto = false; // Variable para indicar si se acertó una letra
    for (let i = 0; i < palabra.length; i++) {
        if (letra == palabra[i]) {
            spans[i].innerHTML = letra; // Mostrar la letra adivinada en la posición correspondiente
            cant_aciertos++; // Incrementar el contador de aciertos
            acerto = true; // Marcar que se ha acertado
        }
    }

    if (!acerto) {
        cant_errores++; // Incrementar el contador de errores
        const source = `img/img${cant_errores}.png`; // Obtener la ruta de la imagen de error
        imagen.src = source; // Mostrar la imagen correspondiente al error

        // Agregar clases de error y vibración al botón
        button.classList.add('error', 'vibrate');
    }

    // Verificar si se ha perdido o ganado el juego
    if (cant_errores == 7) {
        id('resultado').innerHTML = "Perdiste, la palabra era " + palabrita; // Mostrar mensaje de pérdida
        game_over(); // Finalizar el juego
    } else if (cant_aciertos == palabrita.length) {
        id('resultado').innerHTML = "GANASTE!! WIIIIII"; // Mostrar mensaje de victoria
        game_over(); // Finalizar el juego
    }
    console.log("la letra " + letra + " en la palabra " + palabra + " ¿existe?: " + acerto); // Mostrar información en la consola
}

// Función para limpiar el juego y prepararlo para una nueva partida
function limpiarJuego() {
    cant_errores = 0; // Reiniciar contador de errores
    cant_aciertos = 0; // Reiniciar contador de aciertos
    palabrita = null; // Reiniciar la palabra a adivinar

    id('resultado').innerHTML = ''; // Limpiar resultado anterior, si lo hay

    // Habilitar todos los botones de letras y remover la clase de error
    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = false;
        btn_letras[i].classList.remove('error'); // Elimina la clase error de los botones
    }

    const parrafo = id('palabra_a_adivinar'); // Obtener el párrafo para la palabra a adivinar
    parrafo.innerHTML = ''; // Limpiar el contenido del párrafo
}

// Evento para iniciar una nueva partida
btn.addEventListener('click', function(event) {
    limpiarJuego(); // Limpiar el juego
    iniciar(event); // Iniciar una nueva partida
});

// Función para finalizar el juego
function game_over() {
    // Deshabilitar todos los botones de letras
    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = true;
    }
    btn.disabled = false; // Habilitar el botón 'jugar'
}

// Función para obtener un número aleatorio entre un rango dado
function obtener_random(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

// Función para obtener un elemento del DOM por su ID
function id(id) {
    return document.getElementById(id);
}
