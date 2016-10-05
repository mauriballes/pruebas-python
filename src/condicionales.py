#encoding: utf-8

# Sentencias condicionales
edad = 18
m_edad = 18

# if
if edad >= m_edad:
    print "Eres mayor de edad"
    if False:
        print "Esto se ejecuta siempre que sea mayor de edad"
    else:
        print "Cualquier cosa"
else:
    print "No eres mayor de edad"

print "Hola esto se ejecuta siempre"

print "###########################"

edad = 16

if edad >= 0 and edad < 18:
    print "Eres un niño"
elif edad >= 18 and edad < 27:
    print "Eres un joven"
elif edad >= 27 and edad < 60:
    print "Eres un adulto"
else:
    print "Eres de la tercera edad"