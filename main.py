from Persona import persona

if __name__ == "__main__":
    
    persona1 = persona(nombre = "", edad = 0, sexo = "", peso = 0, altura = 0)
    persona2 = persona(nombre = "", edad = 0, sexo = "", peso = 0, altura = 0.0)
    persona3 = persona("Juan",  35, "M", 75, 1.70)
    
    persona1.setNombre(input("Digite un nombre: "))
    persona1.setEdad(input("Digite su edad: "))
    persona1.setSexo(input("Digite su sexo: "))
    persona1.setPeso(input("Digite su peso: "))
    persona1.setAltura(input("Digite su altura: "))
    print("\n")
    persona2.setNombre(input("Digite un nombre: "))
    persona2.setEdad(input("Digite su edad: "))
    persona2.setSexo(input("Digite su sexo: "))
    #print("\n")
    #persona3.generacioncc()
    

    print("\n")
    print("Atributos Objeto 1: ")
    print(" Nombre: %s \n Edad: %d \n Sexo: %s \n Peso: %d \n Altura: %f " % (persona1.getNombre(), persona1.getEdad(), persona1.getSexo(), persona1.getPeso(), persona1.getAltura()))
    persona1.generacioncc()
    persona1.calcularimc() 
    persona1.mayorDeEdad()
    
    print("\n")
    print("Atributos Objeto 2: ")
    print(" Nombre: %s \n Edad: %d \n Sexo: %s " % (persona2.getNombre(), persona2.getEdad(), persona2.getSexo()))
    persona2.generacioncc()
    persona2.mayorDeEdad()
    
    print("\n")
    print("Atributos Objeto 3: ")
    print(" Nombre: %s \n Edad: %d \n Sexo: %s \n Peso: %d \n Altura: %f " % (persona3.getNombre(), persona3.getEdad(), persona3.getSexo(), persona3.getPeso(), persona3.getAltura()))
    persona3.generacioncc()
    persona3.calcularimc()
    persona3.mayorDeEdad()
   
    





