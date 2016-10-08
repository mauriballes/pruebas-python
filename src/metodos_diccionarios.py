#encoding: utf-8

diccionario = {
    'redes_sociales': ["Twitter", "Facebook", "LinkedIn"],
    3: "Tres",
    'Hola': "Mundo"
}

# has_key (pregunta si existe esa llave)
print diccionario.has_key(4)

# items (devuelve una lista de tuplas)
# el 1er elem de la tupla es la clave
# y el 2do es elemento
print diccionario.items()

# keys (devuelve lista de claves)
print diccionario.keys()

# values (devuelve una lista de valores)
print diccionario.values()

# pop (devuelve el valor del elem y los borra)
# DICCIONARIO.pop(clave, d)
# d => (opcional)
# d = valor para devolver en caso de no encontrar la clave
print diccionario
diccionario.pop(4, -1)
print diccionario

# Eliminar un elemento
print diccionario
del diccionario['Hola']
print diccionario

# Eliminar todos los elem del diccionario
print diccionario
diccionario.clear()
print diccionario

# Adicionar nuevo elemento
# No Se necesita un metodo para agregar nuevos valores
diccionario['clave_nueva'] = 'Valor'
print diccionario

# Copy
diccionario_2 = diccionario.copy()
print diccionario_2