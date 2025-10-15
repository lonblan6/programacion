# SETS EN PYTHON
# Los sets son colecciones no ordenadas de elementos únicos

# Creación de sets
numeros = {1, 2, 3, 4, 5}
colores = {"rojo", "verde", "azul", "rojo"}  # El duplicado se elimina automáticamente
mixto = {1, "hola", 3.14, True}

print("Sets creados:")
print(f"Números: {numeros}")
print(f"Colores: {colores}")  # Solo mostrará colores únicos
print(f"Mixto: {mixto}")

# Creación desde lista (elimina duplicados)
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4]
set_sin_duplicados = set(lista_con_duplicados)
print(f"\nLista original: {lista_con_duplicados}")
print(f"Set sin duplicados: {set_sin_duplicados}")

# Set vacío
set_vacio = set()  # No usar {} porque crea un diccionario
print(f"Set vacío: {set_vacio}")

# Operaciones básicas
print(f"\nLongitud del set: {len(numeros)}")
print(f"¿Está 3 en números?: {3 in numeros}")
print(f"¿Está 10 en números?: {10 in numeros}")

# Agregar elementos
numeros.add(6)
numeros.add(3)  # No se duplica
print(f"Números después de agregar 6 y 3: {numeros}")

# Eliminar elementos
numeros.remove(6)  # Error si no existe
print(f"Después de remover 6: {numeros}")

numeros.discard(10)  # No da error si no existe
print(f"Después de descartar 10: {numeros}")

# Operaciones entre sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")

# Unión
union = set1 | set2  # o set1.union(set2)
print(f"Unión: {union}")

# Intersección
interseccion = set1 & set2  # o set1.intersection(set2)
print(f"Intersección: {interseccion}")

# Diferencia
diferencia = set1 - set2  # o set1.difference(set2)
print(f"Diferencia (set1 - set2): {diferencia}")

# Diferencia simétrica
diferencia_simetrica = set1 ^ set2  # o set1.symmetric_difference(set2)
print(f"Diferencia simétrica: {diferencia_simetrica}")

# Verificar subconjuntos
subset = {1, 2, 3}
print(f"\n¿{{1,2,3}} es subconjunto de set1?: {subset.issubset(set1)}")
print(f"¿set1 contiene {{1,2,3}}?: {set1.issuperset(subset)}")

# Casos de uso comunes:

# 1. Eliminar duplicados de una lista
lista_duplicados = [1, 2, 2, 3, 3, 4, 4, 5]
lista_unica = list(set(lista_duplicados))
print(f"\nLista con duplicados: {lista_duplicados}")
print(f"Lista sin duplicados: {lista_unica}")

# 2. Verificar elementos únicos en dos listas
estudiantes_curso_a = {"Ana", "Luis", "María", "Carlos"}
estudiantes_curso_b = {"Luis", "Carlos", "Pedro", "Sofia"}

solo_en_a = estudiantes_curso_a - estudiantes_curso_b
solo_en_b = estudiantes_curso_b - estudiantes_curso_a
en_ambos = estudiantes_curso_a & estudiantes_curso_b

print(f"\nEstudiantes solo en curso A: {solo_en_a}")
print(f"Estudiantes solo en curso B: {solo_en_b}")
print(f"Estudiantes en ambos cursos: {en_ambos}")

# 3. Verificar si una palabra tiene letras únicas
palabra = "python"
letras_unicas = set(palabra)
print(f"\nPalabra: {palabra}")
print(f"Letras únicas: {letras_unicas}")
print(f"¿Tiene letras repetidas?: {len(palabra) != len(letras_unicas)}")

# 4. Filtrado de datos
usuarios_activos = {"user1", "user2", "user3", "user4"}
usuarios_premium = {"user1", "user3", "user5"}

usuarios_activos_premium = usuarios_activos & usuarios_premium
print(f"\nUsuarios activos y premium: {usuarios_activos_premium}")

# Iteración (sin orden específico)
print("\nIterando sobre el set:")
for elemento in numeros:
    print(f"Elemento: {elemento}")
