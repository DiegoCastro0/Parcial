class viaje:
    def __init__(self, destino, duracion, precio, TF, TH):
        self.destino = destino
        self.duracion = duracion
        self.precio = precio
        self.TF = TF
        self.TH = TH

    def mostrar_info(self):
        return f"Destino: {self.destino}, Duración: {self.duracion} horas, Precio: ${self.precio}"

    def calcular_TF(self):
        if self.TF:
            return self.precio * 7
        else:
            return self.precio
    def calcular_hora(self):
        return self.duracion * 7
