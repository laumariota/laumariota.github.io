#4. diseñe una app con una funcion que calcule el area de un cuadrado y sea llamda por un algoritmo
def areas():
    area=(base*altura)/2
    print("el area de un cuadrado es: ",area)

base=float(input("Digite la base de un cuadrado: "))
altura=float(input("Digite la altura de un cuadrado: "))

areas() #llamando a la funcion