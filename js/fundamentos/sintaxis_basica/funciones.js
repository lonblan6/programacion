// FUNCIONES EN JAVASCRIPT

// 1. Declaración de función (Function Declaration)
console.log("=== DECLARACIÓN DE FUNCIÓN ===");
function saludar(nombre) {
    return `¡Hola, ${nombre}!`;
}

console.log(saludar("Juan Carlos"));

// 2. Expresión de función (Function Expression)
console.log("\n=== EXPRESIÓN DE FUNCIÓN ===");
const sumar = function(a, b) {
    return a + b;
};

console.log(`Suma: ${sumar(5, 3)}`);

// 3. Arrow Functions (ES6)
console.log("\n=== ARROW FUNCTIONS ===");
const multiplicar = (a, b) => a * b;
const cuadrado = x => x * x;
const saludarSinParametros = () => "¡Hola mundo!";

console.log(`Multiplicación: ${multiplicar(4, 3)}`);
console.log(`Cuadrado: ${cuadrado(5)}`);
console.log(`Saludo: ${saludarSinParametros()}`);

// 4. Parámetros por defecto
console.log("\n=== PARÁMETROS POR DEFECTO ===");
function crearUsuario(nombre, edad = 18, ciudad = "Desconocida") {
    return {
        nombre: nombre,
        edad: edad,
        ciudad: ciudad
    };
}

console.log("Usuario con todos los parámetros:");
console.log(crearUsuario("Ana", 25, "Madrid"));

console.log("Usuario con parámetros por defecto:");
console.log(crearUsuario("Luis"));

// 5. Rest Parameters (...)
console.log("\n=== REST PARAMETERS ===");
function sumarTodos(...numeros) {
    let suma = 0;
    for (let numero of numeros) {
        suma += numero;
    }
    return suma;
}

console.log(`Suma de 1,2,3: ${sumarTodos(1, 2, 3)}`);
console.log(`Suma de 1,2,3,4,5: ${sumarTodos(1, 2, 3, 4, 5)}`);

// 6. Destructuring en parámetros
console.log("\n=== DESTRUCTURING EN PARÁMETROS ===");
function mostrarUsuario({nombre, edad, profesion}) {
    return `${nombre} tiene ${edad} años y es ${profesion}`;
}

const usuario = {
    nombre: "Carlos",
    edad: 30,
    profesion: "Programador"
};

console.log(mostrarUsuario(usuario));

// 7. Funciones como valores
console.log("\n=== FUNCIONES COMO VALORES ===");
const operaciones = {
    sumar: (a, b) => a + b,
    restar: (a, b) => a - b,
    multiplicar: (a, b) => a * b,
    dividir: (a, b) => a / b
};

console.log(`5 + 3 = ${operaciones.sumar(5, 3)}`);
console.log(`10 - 4 = ${operaciones.restar(10, 4)}`);

// 8. Callbacks
console.log("\n=== CALLBACKS ===");
function procesarArray(array, callback) {
    const resultado = [];
    for (let i = 0; i < array.length; i++) {
        resultado.push(callback(array[i]));
    }
    return resultado;
}

const numeros = [1, 2, 3, 4, 5];
const cuadrados = procesarArray(numeros, x => x * x);
const dobles = procesarArray(numeros, x => x * 2);

console.log(`Números originales: ${numeros}`);
console.log(`Cuadrados: ${cuadrados}`);
console.log(`Dobles: ${dobles}`);

// 9. Funciones de orden superior
console.log("\n=== FUNCIONES DE ORDEN SUPERIOR ===");
const crearMultiplicador = (factor) => {
    return (numero) => numero * factor;
};

const multiplicarPor2 = crearMultiplicador(2);
const multiplicarPor3 = crearMultiplicador(3);

console.log(`5 * 2 = ${multiplicarPor2(5)}`);
console.log(`5 * 3 = ${multiplicarPor3(5)}`);

// 10. Closures
console.log("\n=== CLOSURES ===");
function crearContador() {
    let contador = 0;
    return function() {
        contador++;
        return contador;
    };
}

const contador1 = crearContador();
const contador2 = crearContador();

console.log(`Contador 1: ${contador1()}`);
console.log(`Contador 1: ${contador1()}`);
console.log(`Contador 2: ${contador2()}`);
console.log(`Contador 1: ${contador1()}`);

// 11. Recursión
console.log("\n=== RECURSIÓN ===");
function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

function fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(`Factorial de 5: ${factorial(5)}`);
console.log(`Fibonacci de 7: ${fibonacci(7)}`);

// 12. Métodos de array que usan funciones
console.log("\n=== MÉTODOS DE ARRAY CON FUNCIONES ===");
const estudiantes = [
    {nombre: "Ana", nota: 85},
    {nombre: "Luis", nota: 92},
    {nombre: "María", nota: 78},
    {nombre: "Carlos", nota: 88}
];

// map() - transformar cada elemento
const nombres = estudiantes.map(estudiante => estudiante.nombre);
console.log(`Nombres: ${nombres}`);

// filter() - filtrar elementos
const aprobados = estudiantes.filter(estudiante => estudiante.nota >= 80);
console.log("Aprobados:");
aprobados.forEach(estudiante => console.log(`  ${estudiante.nombre}: ${estudiante.nota}`));

// reduce() - reducir a un valor
const promedio = estudiantes.reduce((suma, estudiante) => suma + estudiante.nota, 0) / estudiantes.length;
console.log(`Promedio: ${promedio.toFixed(2)}`);

// 13. Async/Await (introducción básica)
console.log("\n=== ASYNC/AWAIT (BÁSICO) ===");
async function obtenerDatos() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Datos obtenidos después de 1 segundo");
        }, 1000);
    });
}

async function ejemploAsync() {
    try {
        const datos = await obtenerDatos();
        console.log(datos);
    } catch (error) {
        console.error("Error:", error);
    }
}

// Descomenta para probar async/await
// ejemploAsync();
