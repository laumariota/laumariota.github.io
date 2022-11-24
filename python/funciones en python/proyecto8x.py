#FUNCION CON PARAMETRO
# 4. diseñe una app con una funcion que calcule el area de un cuadrado y sea llamda por un algoritmo
def areas(base,altura):
    area=(base*altura)/2
    print("el area de un cuadrado es: ",area)

#app que calcule el area de un cuadrado 
b=float(input("Digite la base de un cuadrado: "))
a=float(input("Digite la altura de un cuadrado: "))

areas(b,a) #llamando a la funcion