#encoding: utf-8

s = "Hola oMuondo"

# Dimension
print len(s)

# Count
# CADENA.count(valor,inicio,fin)
print s.count("o", 0, 4)
print s.count("o",5)

# lower y upper
print s.lower()
print s.upper()

# replace
# CADENA.replace(valor,nuevo,repeticiones)
print s.replace("o","x")
print s.replace("o","x", 2)
print s.replace("Hola","x")

# split (Devuelve una lista)
# CADENA.split(separador, maxsplit)
print s.split("o")
print s.split("o", 2)
print s.split() # Separa por espacios

# find
# CADENA.find(valor,inicio,fin)
print s.find("o")
# rfind (busca de atras para adelante)
print s.rfind("o")

# join
# CADENA.join(secuencia)
t = ("H","o","l","a")
s = ";"
print s.join(t) # H;o;l;a
