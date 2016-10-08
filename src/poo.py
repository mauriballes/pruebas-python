#encoding: utf-8
# POO
class Humano:
    # Constructor
    def __init__(self, edad):
        self.edad = edad

    def hablar(self, mensaje):
        print mensaje

#Herencia
class IngSistemas(Humano):
    def __init__(self):
        print "Hola"

    def programar(self, lenguaje):
        print "Voy a programar en", lenguaje

class LicDerecho(Humano):
    def estudiar_caso(self, caso):
        print "Debo estudiar el caso:", caso

pedro = IngSistemas()
raul = LicDerecho(21)

pedro.programar("Python")
raul.estudiar_caso("Caso Millonario")

pedro.hablar("Hola")
raul.hablar("Hola Pedro")