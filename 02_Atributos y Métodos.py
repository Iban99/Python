class Celular():
    marca = "samsung"
    modelo = "s23"
    camara = "48MP"
#Las variables están creadas únicamente para los objetos instanciados.

#Atributos/Propiedades de instancia
class Celular:
    def __init__(self, marca, modelo, camara): #método constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1= Celular('samsung', 's23', '48MP')
celular2= Celular('apple', 'iphone 15', '48MP')

print(celular1.marca)
print(celular2.modelo)

#Métodos de instancia
class Celular:
    def __init__(self, marca, modelo, camara): #método constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f"Estas haciendo una llamada desde un: {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada desde un: {self.modelo}")

celular1= Celular('samsung', 's23', '48MP')
print(celular1.llamar())


