#FUNCION SIN PARAMETROS
# 1. diseñe una app que calcule el area del rectangulo y luego sea llamada por un algoritmo
def areas():
    area=base*altura
    print("el area del rectangulo es: ",area)

base=float(input("Digite la base del Rectangulo: "))
altura=float(input("Digite la altura del Rectangulo: "))

areas() #llamando a la funcion