let palabrita;
let cant_errores = 0;
let cant_aciertos = 0;
let pistasUsadas = [];

const palabras = [
    'Arbol',
    'Regalo',
    'Trineo',
    'Renos',
    'Velas',
    'Mazapan',
    'Nochevieja',
    'Turron'
];

const btn = document.getElementById('jugar');
const btnAyuda = document.getElementById('ayuda');
const imagen = document.getElementById('imagen');
const btn_letras = document.querySelectorAll("#letras button");

btn.addEventListener('click', iniciar);
btnAyuda.addEventListener('click', mostrarAyuda);

function iniciar(event) {
    limpiarJuego();

    const parrafo = document.getElementById('palabra_a_adivinar');
    parrafo.innerHTML = '';

    const cant_palabras = palabras.length;
    const valor_al_azar = obtener_random(0, cant_palabras);

    palabrita = palabras[valor_al_azar];
    console.log(palabrita);
    const cant_letras = palabrita.length;

    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = false;
    }

    for (let i = 0; i < cant_letras; i++) {
        const span = document.createElement('span');
        parrafo.appendChild(span);
    }
}

for (let i = 0; i < btn_letras.length; i++) {
    btn_letras[i].addEventListener('click', click_letras);
}

function click_letras(event) {
    const spans = document.querySelectorAll('#palabra_a_adivinar span');
    const button = event.target;
    button.disabled = true;

    const letra = button.innerHTML.toLowerCase();
    const palabra = palabrita.toLowerCase();

    let acerto = false;
    for (let i = 0; i < palabra.length; i++) {
        if (letra == palabra[i]) {
            spans[i].innerHTML = letra;
            cant_aciertos++;
            acerto = true;
        }
    }

    if (!acerto) {
        cant_errores++;
        const source = `img/img${cant_errores}.png`;
        imagen.src = source;

        // Agregar clases de error y vibración al botón
        button.classList.add('error', 'vibrate');
    }

    if (cant_errores == 7) {
        document.getElementById('resultado').innerHTML = "Perdiste, la palabra era " + palabrita;
        game_over();
    } else if (cant_aciertos == palabrita.length) {
        document.getElementById('resultado').innerHTML = "¡GANASTE!";
        game_over();
    }
    console.log("La letra " + letra + " en la palabra " + palabra + " ¿existe?: " + acerto);
}

function mostrarAyuda() {
    const parrafoAyuda = document.getElementById('ayuda-texto');

    const pistas = obtenerPistas(palabrita);

    if (pistasUsadas.length >= pistas.length) {
        parrafoAyuda.innerHTML = 'No hay más pistas disponibles.';
        return;
    }

    const pistaActual = pistas[pistasUsadas.length];
    pistasUsadas.push(pistaActual);

    const contenidoPistas = pistasUsadas.map((pista, index) => `${index + 1}. ${pista}<br>`).join('');

    parrafoAyuda.innerHTML = contenidoPistas;
}

function obtenerPistas(palabra) {
    const pistas = {
        'Arbol': ['Se decora con luces y adornos.', 'Es verde y suele ser de pino.', 'Es tradición colocar un adorno especial en la parte superior.',
            'Algunos son artificiales y se pueden reutilizar cada año.'],
        'Regalo': ['Se intercambian en Navidad.', 'Puede estar envuelto con papel de colores.', 'Son intercambiados como muestra de afecto y celebración.',
            'Pueden contener desde juguetes hasta artículos personales.'],
        'Trineo': ['Lo utiliza Papá Noel para repartir regalos.', 'Tiene renos que lo jalan.', 'A menudo se representa como volando en la noche.',
            'Se asocia con la entrega de obsequios durante la Navidad.'],
        'Renos': ['Animales que jalan el trineo de Papá Noel.', 'Uno de ellos tiene una nariz roja.', 'Uno de ellos se llama Rudolph.',
            'Tienen nombres que a menudo están relacionados con la Navidad.'],
        'Velas': ['Se encienden para dar ambiente festivo.', 'Pueden tener fragancias navideñas.', 'A menudo se colocan en un candelabro especial.',
            'Se usan para contar los días de adviento.'],
        'Mazapan': ['Dulce típico de Navidad hecho con almendras y azúcar.', 'Se suele comer en las fiestas navideñas.', 'Se modela en diferentes formas y figuras.',
            'Es popular en varios países europeos durante la temporada navideña.'],
        'Nochevieja': ['Noche del 31 de diciembre, víspera del Año Nuevo.', 'Se celebran con fuegos artificiales y brindis.',
            'Se realizan distintas tradiciones para atraer la buena suerte.'],
        'Turron': ['Es un dulce duro.', 'Se suele comer como postre.', 'Hay variedades de almendra y otras con chocolate.',
            'Se encuentra en diferentes versiones regionales en todo el mundo.']
    };

    return pistas[palabra] || ['No hay pistas disponibles para esta palabra.'];
}

function game_over() {
    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = true;
    }

    btn.disabled = false;
}

function limpiarJuego() {
    cant_errores = 0;
    cant_aciertos = 0;
    palabrita = null;
    pistasUsadas = [];

    document.getElementById('resultado').innerHTML = '';

    for (let i = 0; i < btn_letras.length; i++) {
        btn_letras[i].disabled = false;
        btn_letras[i].classList.remove('error', 'vibrate');
    }

    const parrafoAyuda = document.getElementById('ayuda-texto');
    parrafoAyuda.innerHTML = '';

    imagen.src = 'img/img0.png';

    const spans = document.querySelectorAll('#palabra_a_adivinar span');
    spans.forEach(span => span.textContent = '');
}

function obtener_random(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}
