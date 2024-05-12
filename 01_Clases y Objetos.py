# Curso Python Orientado a Objetos -Soy Dalto-, youtube
celular1_marca= "samsung"
celular2_marca = "apple"

celular1_modelo="s23"
celular2_modelo="iphone 15 pro"

celular1_camaraF= "48MP"
celular2_camaraF= "24MP"

celular1_camaraT= "24MP"
celular2_camaraT= "28MP"

celulares = []
celulares[0] = ['samsung', 's23', '48MP', '28']

# Sintaxis de una CLASE (PascalCase)
class NombreClase():
    propiedad1 = "Valor1"
    propiedad2 = "Valor2"
    propiedad3 = "Valor3"
    
# Ejemplo
class Celular():
    marca = "samsung"
    modelo = "s23"
    camara = "48MP"
    #Propiedades estáticas del objeto

# Creación objeto a partir de clase
celular1 = Celular()
#Consulta de propiedades del objeto
print(celular1.marca) 
print(celular1.modelo)
