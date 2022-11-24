#FUNCION CON PARAMETRO
# 3. diseñe una app con una funcion que calcule el area de un circulo y sea llamda por un algoritmo
def areas(radio):
    area=(radio*2)*3.14
    print("el area de un circulo es: ",area)

r=float(input("Digite el radio del circulo: "))

areas(r)#llamando a la funcion
