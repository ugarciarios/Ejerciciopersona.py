import random

class persona:
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.cedula = 0
      
    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        self.sexo = sexo

    def setPeso(self, peso):
        self.peso = peso

    def setAltura(self, altura):
        self.altura = altura

    def getNombre(self):
        return self.nombre 

    def getEdad(self):
        return int(self.edad)

    def getSexo(self):
        return self.sexo

    def getPeso(self):
        return int(self.peso)

    def getAltura(self):
        return float(self.altura)
    

    def generacioncc(self):
        self.cedula = random.randint(0,99999999)
        print(" Numero de documento: %d " % (self.cedula))

    def calcularimc(self):
        imc = int(self.peso) / float(self.altura)
        if (imc<20):
            print (" Tiene un peso debajo del indicado ")

        elif (imc >= 20 and imc <= 25):
            print (" Tiene un peso promedio ")

        else :
            print (" Tiene sobrepeso ")

    
    def mayorDeEdad(self):
        edad1 = (self.edad)
        if (int(edad1) > 18):
            print(" Es mayor de edad \n")
        
        else :
            print(" Es menor de edad \n")


