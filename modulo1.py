#creamos la clase viaje
class viaje:
    #creamos el metodo constructor de la clase viaje con sus respectivos atributos(destino,duracion,precio,TF,TH)
    def __init__(self, destino, duracion, precio, TF, TH):
        self.destino = destino
        self.duracion = duracion
        self.precio = precio
        self.TF = TF
        self.TH = TH
        
    #creamos un metodo para mostrar la informacion del viaje
    def mostrar_info(self):
        return f"Destino: {self.destino}, Duración: {self.duracion} horas, Precio: ${self.precio}"
    
    #creamos un metodo para calcular el gasto total semanal si es tarifa fija(TF) o tarifa por hora(TH)
    def calcular_TF(self):
        if self.TF:
            return self.precio * 7
        else:
            return self.precio
    
    #creamos un metodo para calcular el total de horas semanales si es tarifa por hora(TH)
    def calcular_hora(self):
        return self.duracion * 7
