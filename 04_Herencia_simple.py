class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("hola estoy hablando un poco")

class Empleado(Persona):
    #pass #Nos permite dejar una clase o una función vacía sin que al llamarla de error
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

roberto = Empleado("Roberto", 43, "argentino", "Programador", 10000)

roberto.hablar()