#app que al ingresar el valor inicial
#y el valor final , muestre los datos
x=int(input("digite el valor inicial: "))
y=int(input("digite el valor final: "))
for i in range(x,y,1):
    print(i)
else:
    print("los valores no son correctos")