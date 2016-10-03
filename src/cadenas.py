# Comillas simples
cads = 'Texto entre \n comillas simples'
# Comillas dobles
cadd = "Texto entre \n\t comillas dobles"

# Comillas triples para que me respete los saltos
# tabulaciones, etc.
cadc = """Texto linea 1
linea 2
linea 3
...
linea n"""

# Caracteres de escape
# \n = salto de linea
# \t = tabulacion

print cads
print cadd
print cadc

# Repeticion y concatenacion
cadr = "Cadena" * 3 # Repeticion
print cadr

cad1 = "Cadena 1"
cad2 = "Cadena 2"
cadc = cad1 + cad2
print cadc

##########################

# Booleanos
bt = True
bf = False

b_and = True and False
b_or = True or False
b_not = not True

print b_and
print b_or
print b_not
