// Función para obtener un elemento del DOM por su ID
function id(str) {
    return document.getElementById(str);
}

// Función para generar un número aleatorio dentro de un rango dado
function obtener_random(num_min, num_max) {
    // Calcula la amplitud de los valores (diferencia entre el valor máximo y mínimo)
    const amplitud_valores = num_max - num_min; // Ejemplo: (7 - 0) = 7

    // Genera un número aleatorio dentro del rango y lo redondea al entero más cercano
    const valor_al_azar = Math.floor(Math.random() * amplitud_valores) + num_min; /* Ejemplo: (Math.random() * 7) + 0 */
    
    // Devuelve el número aleatorio generado
    return valor_al_azar;
}
