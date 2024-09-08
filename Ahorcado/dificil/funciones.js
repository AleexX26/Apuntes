// Función que devuelve un elemento del DOM basado en su ID
function id(str) {
    return document.getElementById(str);
}

// Función que genera un número aleatorio dentro de un rango específico
function obtener_random(num_min, num_max) {
    // Calcula la amplitud de valores posibles dentro del rango dado
    const amplitud_valores = num_max - num_min;

    // Genera un número aleatorio decimal entre 0 (inclusive) y 1 (exclusivo),
    // lo multiplica por la amplitud de valores y le suma el valor mínimo
    const valor_al_azar = Math.floor(Math.random() * amplitud_valores) + num_min;

    return valor_al_azar; // Devuelve el número aleatorio dentro del rango especificado
}
