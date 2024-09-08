// Función para obtener un elemento del DOM por su ID
function id(str) {
    return document.getElementById(str);
}

// Función para generar un número aleatorio dentro de un rango específico
function obtener_random(num_min, num_max) {
    // Calcula la amplitud de valores dentro del rango
    const amplitud_valores = num_max - num_min;
    
    // Genera un número aleatorio entre 0 y la amplitud de valores,
    // luego se suma el valor mínimo para obtener un número dentro del rango deseado
    const valor_al_azar = Math.floor(Math.random() * amplitud_valores) + num_min;
    
    return valor_al_azar; // Retorna el número aleatorio obtenido
}
