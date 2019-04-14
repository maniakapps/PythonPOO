#Creando una nueva clase
class Carro:
    def __init__(self, make, model, year):
        self.marca = make
        self.modelo = model
        self.anio = year

    def __str__(self):
        print("Marca: {} \n Modelo: {} \n Año: {}".format(self.marca, self.modelo, self.anio))
        
#Creando otra clase
class Dog:
    pass

