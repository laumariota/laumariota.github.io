#fucion de horas a minutos
def convertir():
    minutos=horas*60
    print("------------------------------")
    print(horas,"horas, son: ", minutos, "minutos")
    print("------------------------------")

horas=int(input("digite la horas que desea convertir a minutos: "))

convertir() #llamada a la funcion