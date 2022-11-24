#funcion de la suma, resta, multiplicacion y divicion (calculadora).
def calculadora():
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    divicion=a/b

    print("°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("la suma es: ",suma)
    print("---------------------")
    print("la resta es: ",resta)
    print("---------------------")
    print("la multiplicacion es: ",multiplicacion)
    print("---------------------")
    print("la divicion es: ",divicion)
    print("_____________________")

a=int(input("Digite el primer numero: "))
b=int(input("Digite el segundo numero: "))

resultado=calculadora() #llamando la funcion suma

