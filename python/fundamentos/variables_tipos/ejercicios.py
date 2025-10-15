# EJERCICIOS DE VARIABLES Y TIPOS DE DATOS

# Ejercicio 1: Información Personal
print("=== EJERCICIO 1: INFORMACIÓN PERSONAL ===")
nombre = "Juan Carlos"
edad = 25
altura = 1.75
estudiante = True

print(f"Nombre: {nombre} (tipo: {type(nombre)})")
print(f"Edad: {edad} (tipo: {type(edad)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
print(f"Es estudiante: {estudiante} (tipo: {type(estudiante)})")

# Ejercicio 2: Operaciones Matemáticas
print("\n=== EJERCICIO 2: OPERACIONES MATEMÁTICAS ===")
num1 = 10
num2 = 3

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {division_entera}")
print(f"{num1} % {num2} = {modulo}")
print(f"{num1} ** {num2} = {potencia}")

# Ejercicio 3: Manipulación de Strings
print("\n=== EJERCICIO 3: MANIPULACIÓN DE STRINGS ===")
texto = "  Programación en Python  "

print(f"Texto original: '{texto}'")
print(f"Longitud: {len(texto)}")
print(f"En mayúsculas: '{texto.upper()}'")
print(f"En minúsculas: '{texto.lower()}'")
print(f"Sin espacios: '{texto.strip()}'")
print(f"Primera palabra: '{texto.strip().split()[0]}'")
print(f"¿Contiene 'Python'?: {'Python' in texto}")

# Ejercicio 4: Conversión de Tipos
print("\n=== EJERCICIO 4: CONVERSIÓN DE TIPOS ===")
numero_str = "42"
numero_float = 3.14
booleano = True

print(f"String '{numero_str}' a entero: {int(numero_str)}")
print(f"String '{numero_str}' a float: {float(numero_str)}")
print(f"Float {numero_float} a entero: {int(numero_float)}")
print(f"Float {numero_float} a string: '{str(numero_float)}'")
print(f"Booleano {booleano} a entero: {int(booleano)}")
print(f"Booleano {booleano} a string: '{str(booleano)}'")

# Ejercicio 5: Formateo de Strings
print("\n=== EJERCICIO 5: FORMATEO DE STRINGS ===")
producto = "Laptop"
precio = 999.99
cantidad = 2

# Método .format()
mensaje1 = "Producto: {}, Precio: ${:.2f}, Cantidad: {}".format(producto, precio, cantidad)
print(f"Con .format(): {mensaje1}")

# f-strings (recomendado)
mensaje2 = f"Producto: {producto}, Precio: ${precio:.2f}, Cantidad: {cantidad}"
print(f"Con f-string: {mensaje2}")

# Ejercicio 6: Operadores de Comparación
print("\n=== EJERCICIO 6: OPERADORES DE COMPARACIÓN ===")
a = 10
b = 5

print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# Ejercicio 7: Operadores Lógicos
print("\n=== EJERCICIO 7: OPERADORES LÓGICOS ===")
edad = 20
tiene_licencia = True
es_estudiante = False

puede_conducir = edad >= 18 and tiene_licencia
descuento_estudiante = edad < 25 or es_estudiante
no_es_menor = not (edad < 18)

print(f"Puede conducir: {puede_conducir}")
print(f"Descuento estudiante: {descuento_estudiante}")
print(f"No es menor de edad: {no_es_menor}")

# Ejercicio 8: Números Complejos
print("\n=== EJERCICIO 8: NÚMEROS COMPLEJOS ===")
z1 = 3 + 4j
z2 = 1 - 2j

print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 * z2 = {z1 * z2}")
print(f"Parte real de z1: {z1.real}")
print(f"Parte imaginaria de z1: {z1.imag}")
print(f"Módulo de z1: {abs(z1)}")

# Ejercicio 9: Trabajo con None
print("\n=== EJERCICIO 9: TRABAJO CON None ===")
valor = None
print(f"Valor inicial: {valor}")
print(f"¿Es None?: {valor is None}")

valor = "Ahora tiene un valor"
print(f"Valor después: {valor}")
print(f"¿Es None?: {valor is None}")

# Ejercicio 10: Verificación de Tipos
print("\n=== EJERCICIO 10: VERIFICACIÓN DE TIPOS ===")
datos = [42, "hola", 3.14, True, None, [1, 2, 3]]

for dato in datos:
    print(f"Valor: {dato}, Tipo: {type(dato).__name__}")
    if isinstance(dato, int):
        print("  → Es un entero")
    elif isinstance(dato, str):
        print("  → Es una cadena")
    elif isinstance(dato, float):
        print("  → Es un flotante")
    elif isinstance(dato, bool):
        print("  → Es un booleano")
    elif isinstance(dato, list):
        print("  → Es una lista")
    else:
        print("  → Otro tipo")
    print()
