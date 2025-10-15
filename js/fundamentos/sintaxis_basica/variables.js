// VARIABLES EN JAVASCRIPT

// Declaración de variables
var nombre = "Juan Carlos";  // var (scope de función, puede ser redeclarada)
let edad = 25;               // let (scope de bloque, no puede ser redeclarada)
const ciudad = "Madrid";     // const (scope de bloque, no puede ser reasignada)

console.log("Variables declaradas:");
console.log(`Nombre: ${nombre}`);
console.log(`Edad: ${edad}`);
console.log(`Ciudad: ${ciudad}`);

// Diferencias entre var, let y const
console.log("\n=== DIFERENCIAS ENTRE var, let y const ===");

// var puede ser redeclarada
var nombre = "Carlos";  // No da error
console.log(`Nombre redeclarado: ${nombre}`);

// let no puede ser redeclarada en el mismo scope
// let edad = 30;  // Error: Identifier 'edad' has already been declared

// const no puede ser reasignada
// ciudad = "Barcelona";  // Error: Assignment to constant variable

// Tipos de datos
console.log("\n=== TIPOS DE DATOS ===");

// Números
let numeroEntero = 42;
let numeroDecimal = 3.14;
let numeroNegativo = -10;

console.log(`Entero: ${numeroEntero} (tipo: ${typeof numeroEntero})`);
console.log(`Decimal: ${numeroDecimal} (tipo: ${typeof numeroDecimal})`);
console.log(`Negativo: ${numeroNegativo} (tipo: ${typeof numeroNegativo})`);

// Strings
let saludo = "Hola";
let nombreCompleto = 'Juan Carlos';
let plantilla = `Mi nombre es ${nombreCompleto}`;

console.log(`Saludo: ${saludo} (tipo: ${typeof saludo})`);
console.log(`Nombre completo: ${nombreCompleto} (tipo: ${typeof nombreCompleto})`);
console.log(`Plantilla: ${plantilla} (tipo: ${typeof plantilla})`);

// Booleanos
let esEstudiante = true;
let tieneTrabajo = false;

console.log(`Es estudiante: ${esEstudiante} (tipo: ${typeof esEstudiante})`);
console.log(`Tiene trabajo: ${tieneTrabajo} (tipo: ${typeof tieneTrabajo})`);

// Valores especiales
let indefinido = undefined;
let nulo = null;
let noEsNumero = NaN;

console.log(`Indefinido: ${indefinido} (tipo: ${typeof indefinido})`);
console.log(`Nulo: ${nulo} (tipo: ${typeof nulo})`);
console.log(`No es número: ${noEsNumero} (tipo: ${typeof noEsNumero})`);

// Operadores aritméticos
console.log("\n=== OPERADORES ARITMÉTICOS ===");
let a = 10;
let b = 3;

console.log(`${a} + ${b} = ${a + b}`);
console.log(`${a} - ${b} = ${a - b}`);
console.log(`${a} * ${b} = ${a * b}`);
console.log(`${a} / ${b} = ${a / b}`);
console.log(`${a} % ${b} = ${a % b}`);
console.log(`${a} ** ${b} = ${a ** b}`);

// Operadores de asignación
console.log("\n=== OPERADORES DE ASIGNACIÓN ===");
let x = 5;
console.log(`x inicial: ${x}`);

x += 3;  // x = x + 3
console.log(`x después de += 3: ${x}`);

x -= 2;  // x = x - 2
console.log(`x después de -= 2: ${x}`);

x *= 2;  // x = x * 2
console.log(`x después de *= 2: ${x}`);

x /= 3;  // x = x / 3
console.log(`x después de /= 3: ${x}`);

// Operadores de comparación
console.log("\n=== OPERADORES DE COMPARACIÓN ===");
let num1 = 10;
let num2 = "10";

console.log(`${num1} == ${num2}: ${num1 == num2}`);   // true (conversión de tipo)
console.log(`${num1} === ${num2}: ${num1 === num2}`); // false (sin conversión)
console.log(`${num1} != ${num2}: ${num1 != num2}`);   // false
console.log(`${num1} !== ${num2}: ${num1 !== num2}`); // true
console.log(`${num1} > 5: ${num1 > 5}`);
console.log(`${num1} < 15: ${num1 < 15}`);
console.log(`${num1} >= 10: ${num1 >= 10}`);
console.log(`${num1} <= 10: ${num1 <= 10}`);

// Operadores lógicos
console.log("\n=== OPERADORES LÓGICOS ===");
let tieneLicencia = true;
let edadConductor = 22;
let esEstudiante = false;

console.log(`Puede conducir (edad >= 18 && tieneLicencia): ${edadConductor >= 18 && tieneLicencia}`);
console.log(`Descuento estudiante (edad < 25 || esEstudiante): ${edadConductor < 25 || esEstudiante}`);
console.log(`No es estudiante (!esEstudiante): ${!esEstudiante}`);

// Conversión de tipos
console.log("\n=== CONVERSIÓN DE TIPOS ===");
let stringNumero = "42";
let numeroDesdeString = Number(stringNumero);
let stringDesdeNumero = String(numeroDesdeString);
let booleanoDesdeNumero = Boolean(numeroDesdeString);

console.log(`String "42" a número: ${numeroDesdeString} (tipo: ${typeof numeroDesdeString})`);
console.log(`Número a string: "${stringDesdeNumero}" (tipo: ${typeof stringDesdeNumero})`);
console.log(`Número a booleano: ${booleanoDesdeNumero} (tipo: ${typeof booleanoDesdeNumero})`);

// Conversiones automáticas (coerción)
console.log("\n=== CONVERSIONES AUTOMÁTICAS ===");
console.log(`"5" + 3: "${"5" + 3}"`);  // "53" (concatenación)
console.log(`"5" - 3: ${"5" - 3}`);    // 2 (resta convierte a número)
console.log(`"5" * 3: ${"5" * 3}`);    // 15 (multiplicación convierte a número)
console.log(`"5" / 3: ${"5" / 3}`);    // 1.666... (división convierte a número)

// Scope de variables
console.log("\n=== SCOPE DE VARIABLES ===");

// Scope global
var variableGlobal = "Soy global";

function ejemploScope() {
    // Scope de función
    var variableFuncion = "Soy de función";
    let variableBloque = "Soy de bloque";
    
    if (true) {
        // Scope de bloque
        let variableBloqueInterno = "Soy de bloque interno";
        var variableFuncionInterna = "Soy de función interna";
        
        console.log(`Dentro del bloque: ${variableBloqueInterno}`);
        console.log(`Variable de función interna: ${variableFuncionInterna}`);
    }
    
    console.log(`Variable de función: ${variableFuncion}`);
    console.log(`Variable de bloque: ${variableBloque}`);
    // console.log(variableBloqueInterno);  // Error: variableBloqueInterno is not defined
}

ejemploScope();
console.log(`Variable global: ${variableGlobal}`);
// console.log(variableFuncion);  // Error: variableFuncion is not defined

// Hoisting (elevación)
console.log("\n=== HOISTING ===");
console.log(`Variable hoisted: ${variableHoisted}`);  // undefined (no error)
var variableHoisted = "Soy hoisted";

// Con let no hay hoisting
// console.log(variableLetHoisted);  // Error: Cannot access 'variableLetHoisted' before initialization
let variableLetHoisted = "Soy let hoisted";
