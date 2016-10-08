#encoding: utf-8

lista = [1, "Dos", 3]
elemento_a_buscar = 1

# Buscar en una lista
print elemento_a_buscar in lista

# Obtener indice
print lista.index(elemento_a_buscar)

if elemento_a_buscar in lista:
    print lista.index(elemento_a_buscar)
else:
    print "No esta en la lista"

# Adicionar elemento a la lista
print lista
lista.append("Nuevo Elemento")
print lista

# Count (Cuenta las veces que se repite)
print lista.count("Dos")

# Insertar(element, new_element)
print lista
lista.insert(2,"Nuevo")
print lista

# Extender una lista
print lista
iterable = [1,2,3,4] # Cadena, tupla o lista
lista.extend(iterable)
print lista

# Pop (se puede mandar un indice)
print lista
lista.pop() #El ultimo
print lista
lista.pop(2)
print lista

# remove (elimina un elemnto de la lista)
print lista
lista.remove(1)
print lista

# reverse (invertir lista)
print lista
lista.reverse()
print lista