#FUNCION CON PARAMETROS
# 2. diseñe una app con una funcion que calcule el area del triangulo y sea llamda por un algoritmo
def areas(b,a):
    area=(b*a)/2
    print("el area del triangulo es: ",area)

#app que calcule el area del triangulo
base=int(input("Digite la base del triangulo: "))
altura=int(input("Digite la altura de un triangulo: "))

areas(base,altura) #llamando a la funcion 
