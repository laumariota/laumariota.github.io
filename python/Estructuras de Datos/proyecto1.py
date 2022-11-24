#for: recorrer una lista
frutas =['apple', 'banana', 'cherry']
#añadimos un elemento a la lista
frutas.append("grape")
frutas.remove("apple")
#recorremos a la lista
for x in frutas:
    print(x)
#definimos un elemento a la lista
longitud = len(frutas)    
print("el tamaño o longitud es: ", longitud)