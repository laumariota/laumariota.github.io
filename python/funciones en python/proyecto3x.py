#funcion con parametro
#(calculadora).
def convertir(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    divicion=a/b
    print("-------------------")
    print("la suma es: ",suma)
    print("-------------------")
    print("la resta es: ",resta)
    print("-------------------")
    print("la multiplicacion es: ",multiplicacion)
    print("-------------------")
    print("la divicion es: ",divicion)
    print("-------------------")

#app que ingrese dos entero y los calcule
n=int(input("Digite el 1er numero: "))
m=int(input("Digite el 2do numero: "))

resultado=convertir(n,m) #llamando a la funcion
