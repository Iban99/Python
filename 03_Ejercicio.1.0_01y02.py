# Definir una clase estudiante
class Estudiante:
    def __init__ (self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'El estudiante {self.nombre} está estudiando')

#Creación del objeto de la instancia estudiante
pedro = Estudiante('Pedro', 23, 3)

#Llamada al objeto y a un atributo
pedro.grado
pedro.edad
