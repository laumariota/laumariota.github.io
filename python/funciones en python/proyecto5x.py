#FUNCION CON PARAMETROS
# 1. diseñe una app que calcule el area del rectangulo y luego sea llamada por un algoritmo
def areas(base,altura):
    area=base*altura
    print("el area del rectangulo es: ",area)

#app que calcule el area del rectangulo
b=float(input("Digite la base del Rectangulo: "))
a=float(input("Digite la altura del Rectangulo: "))

areas(b,a) #llamando a la funcion