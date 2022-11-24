#fucion con parametros
#de horas a minutos
def convertir(hora):
    minutos=hora*60
    print("------------------------------")
    print(horas,"horas, son: ", minutos, "minutos")
    print("------------------------------")

horas=int(input("digite la horas que desea convertir a minutos: "))

convertir(horas) #llamada a la funcion