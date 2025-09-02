import modulo1

viaje = modulo1.viaje

lista_viajes = []
while True:
    destino = input("Ingrese el destino del viaje (o 'salir' para terminar): ")
    if destino.lower() == 'salir':
        break
    duracion = float(input("Ingrese la duracion del viaje(horas): "))
    precio = float(input("Ingrese el precio del viaje(diario): "))
    TF = input("¿El viaje es de tarifa fija semanal? (s/n): ").lower() == 's'
    TH = input("¿El viaje es de tarifa por hora? (s/n): ").lower() == 's'

    viaje1 = viaje(destino, duracion, precio, TF,TH)
    lista_viajes.append(viaje1)

print("\nLista de viajes y sus totales:")
for i, v in enumerate(lista_viajes, start=1):
    total = v.calcular_TF()
    total_hora = v.calcular_hora()
    
    print(f"{i}. {v.destino} - gasto total(semanal): ${total:.2f} total tiempo(semanal): {total_hora} horas")
    
    
    