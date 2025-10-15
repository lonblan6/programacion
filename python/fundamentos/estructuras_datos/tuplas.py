# TUPLAS EN PYTHON
# Las tuplas son inmutables (no se pueden modificar después de crearse)

# Creación de tuplas
coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")
mixta = (1, "hola", 3.14, True)

print("Tuplas creadas:")
print(f"Coordenadas: {coordenadas}")
print(f"Colores: {colores}")
print(f"Mixta: {mixta}")

# Acceso a elementos
print(f"\nPrimer color: {colores[0]}")
print(f"Último color: {colores[-1]}")

# Slicing en tuplas
print(f"Primeros dos colores: {colores[0:2]}")

# Operaciones básicas
print(f"\nLongitud de colores: {len(colores)}")
print(f"'rojo' está en colores: {'rojo' in colores}")

# Concatenación de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
concatenada = tupla1 + tupla2
print(f"\nTupla concatenada: {concatenada}")

# Repetición
repetida = tupla1 * 2
print(f"Tupla repetida: {repetida}")

# Diferencia clave con listas: las tuplas son inmutables
# Esto NO funcionará:
# coordenadas[0] = 15  # Error: 'tuple' object does not support item assignment

# Casos de uso comunes:
# 1. Coordenadas geográficas
latitud, longitud = (40.7128, -74.0060)
print(f"\nCoordenadas NYC: Lat {latitud}, Lon {longitud}")

# 2. Retorno múltiple de funciones
def dividir_y_resto(a, b):
    return a // b, a % b

cociente, resto = dividir_y_resto(17, 5)
print(f"17 ÷ 5 = {cociente} con resto {resto}")

# 3. Diccionarios con claves compuestas
puntos = {
    (0, 0): "origen",
    (1, 1): "esquina"
}
print(f"Punto origen: {puntos[(0, 0)]}")
