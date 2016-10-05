#encoding: utf-8

# Bucles
# while
edad = 0

while edad <= 20:
    if edad == 15:
        # Cuando se ejecuta continue dentro
        # de un bucle, se salta esta ejecucion
        # del bucle
        edad += 1
        continue
    elif edad == 18:
        # La palabra break rompe el bucle
        break
    print "Tienes " + str(edad)
    edad += 1

# for
lista = ["Elemento 1", "Elemento 2", "Elemento 3"]

# Por cada elemento de la lista
# iterar y colocar el valor en la
# variable elem
for elem in lista:
    print elem

# Para cadenas
for letra in "Cadena":
    print letra