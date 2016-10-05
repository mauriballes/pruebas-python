#encoding: utf-8

# Funciones
def mi_funcion(num1 = 0, num2 = 0):
    print num1 + num2

# Si colocamos una variable con un *
# Cada parametro extra que mandamos
# nos lo pone en una tupla con el nombre
# de esa variable

def print_cadena(cad, v = 2, *algomas):
    print cad * v

# Si colocamos 2 asteriscos, lo reconocera
# como un diccionario
def mi_second(cad, **algomas):
    print algomas["Carlos"]

def suma(num1, num2):
    return num1 + num2

mi_funcion(3)
print_cadena("Hola", 5, "Adios", "N", "Cadenas")
# Para mandar el parametro al diccionario
# colocar Clave = Valor
mi_second("Hola", Carlos = 5)

resultado = suma(3, 4)
print resultado