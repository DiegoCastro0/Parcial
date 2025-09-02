#importamos la clase viaje del modulo1
import modulo1

#creamos un alias para la clase viaje
viaje = modulo1.viaje

#lista para almacenar los viajes
lista_viajes = []

#Creamos una funcion para agregar los viajes y su informacion a la lista
while True:
    #pedimos al usuario que ingrese los datos del viaje(como destino,duracion,precio,tarifa fija semanal y tarifa por hora)
    destino = input("Ingrese el destino del viaje (o 'salir' para terminar): ")
    if destino.lower() == 'salir':
        break
    duracion = float(input("Ingrese la duracion del viaje(horas): "))
    precio = float(input("Ingrese el precio del viaje(diario): "))
    TF = input("¿El viaje es de tarifa fija semanal? (s/n): ").lower() == 's'
    TH = input("¿El viaje es de tarifa por hora? (s/n): ").lower() == 's'

    #creamos una instancia de la clase viaje con los datos ingresados
    viaje1 = viaje(destino, duracion, precio, TF,TH)
    #agregamos la instancia a la lista de viajes
    lista_viajes.append(viaje1)

#mostramos la informacion de cada viaje y su gasto total semanal y total tiempo semanal
print("\nLista de viajes y sus totales:")
#iteramos sobre la lista de viajes y mostramos su informacion
for i, v in enumerate(lista_viajes, start=1):
    total = v.calcular_TF()
    total_hora = v.calcular_hora()
    #mostramos la informacion del viaje junto con su gasto total semanal y total tiempo semanal
    print(f"{i}. {v.destino} - gasto total(semanal): ${total:.2f} total tiempo(semanal): {total_hora} horas")
    
    
    