#encoding: utf-8
# POO
class Humano:
    # Constructor
    def __init__(self, edad):
        self.edad = edad

    def hablar(self, mensaje):
        print self.edad
        print mensaje

pedro = Humano(26)
raul = Humano(21)

print "Soy Pedro y tengo ", pedro.edad
print "Soy Raul y tengo ", raul.edad

pedro.hablar("Hola")
raul.hablar("Hola Pedro")