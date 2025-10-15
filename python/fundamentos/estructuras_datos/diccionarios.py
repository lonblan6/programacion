# DICCIONARIOS EN PYTHON
# Los diccionarios almacenan pares clave-valor

# Creación de diccionarios
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Programador"
}

# Diccionario vacío
vacío = {}
otro_vacío = dict()

print("Diccionario persona:")
print(persona)

# Acceso a valores
print(f"\nNombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")

# Método get() (más seguro)
print(f"Ciudad: {persona.get('ciudad', 'No especificada')}")
print(f"Teléfono: {persona.get('telefono', 'No especificado')}")

# Modificación y adición
persona["edad"] = 26  # Modificar
persona["telefono"] = "123-456-789"  # Agregar nueva clave
print(f"\nDespués de modificar: {persona}")

# Eliminación
del persona["telefono"]
print(f"Después de eliminar teléfono: {persona}")

# Métodos útiles
print(f"\nClaves: {list(persona.keys())}")
print(f"Valores: {list(persona.values())}")
print(f"Pares clave-valor: {list(persona.items())}")

# Iteración
print("\nIterando por claves:")
for clave in persona:
    print(f"{clave}: {persona[clave]}")

print("\nIterando por items:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Diccionarios anidados
empresa = {
    "nombre": "TechCorp",
    "empleados": {
        "jefe": {
            "nombre": "Ana",
            "salario": 50000
        },
        "desarrollador": {
            "nombre": "Luis",
            "salario": 40000
        }
    }
}

print(f"\nEmpresa: {empresa['nombre']}")
print(f"Jefe: {empresa['empleados']['jefe']['nombre']}")
print(f"Salario del jefe: {empresa['empleados']['jefe']['salario']}")

# Comprobaciones
print(f"\n'nombre' está en persona: {'nombre' in persona}")
print(f"'apellido' está en persona: {'apellido' in persona}")

# Diccionario desde listas
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
personas = dict(zip(nombres, edades))
print(f"\nDiccionario desde listas: {personas}")

# Comprensión de diccionarios
cuadrados = {x: x**2 for x in range(1, 6)}
print(f"Cuadrados: {cuadrados}")

# Casos de uso comunes:
# 1. Contador de elementos
texto = "programacion"
contador = {}
for letra in texto:
    contador[letra] = contador.get(letra, 0) + 1
print(f"\nContador de letras: {contador}")

# 2. Configuración de aplicación
config = {
    "debug": True,
    "puerto": 8080,
    "base_datos": "sqlite:///app.db"
}
print(f"Configuración: {config}")
