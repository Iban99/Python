#### Herencia jerárquica
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
        
class Estudiante(Persona):
    def __init__(self,nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas=notas
        self.universidad=universidad

roberto = Empleado("Roberto", 43, "argentino", "Programador", 10000)

roberto.hablar()

#### Herencia múltiple
class Artista:
    def __init__(self, habilidad):
        self.habilidad=habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self,nombre,edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario=salario
        self.empresa=empresa
    
    def presentarse(self):
        print(f'Hola soy: {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}') #Con el super, siempre llamamos al método padre. Con self no.
        
        
roberto = EmpleadoArtista("Roberto", 43, "argentino", "Cantar", 10000, "CSI")

roberto.presentarse()