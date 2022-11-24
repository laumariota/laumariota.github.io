#recorre las lista vacia de un vehiculo
marcas=[]
modelos=[]
colores=[]
combustibles=[]
cilindrajes=[]
precios=[]
#se define un tamaño para la lista del vehiculo
tamaño=int(input("tamaño de listas de vehiculos: "))
#se recorre la lista del tamaño definido
for i in range(tamaño):
    print("por favor ingrese los datos del vehiculo: ", i+1)
    marca=input("la Marca del Vehiculo es: ")
    modelo=input("el modelo del vehiculo es: ")
    color=input("color del vehiculo: ")
    combustible=input("combustible del vehiculo es: ")
    cilindraje=input("el cilindraje del vehiculo es: ")
    precio=input("precio del vehiculo: ")              
    marcas.append(marca)
    modelos.append(modelo)
    colores.append(color)
    combustibles.append(combustible)
    cilindrajes.append(cilindraje)
    precios.append(precio)
print("Informacion del vehiculo: ")
for i in range(tamaño):
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("la Marca del Vehiculo es:", marcas[i]) 
    print("----------------------------------------------")
    print("el modelo del vehiculo es: ",modelos[i])
    print("----------------------------------------------")
    print("color del vehiculo: ",colores[i])
    print("----------------------------------------------")
    print("combustible del vehiculo es: ", combustibles[i])
    print("----------------------------------------------")
    print("el cilindraje del vehiculo es: ",cilindrajes[i])  
    print("----------------------------------------------")  
    print("precio del vehiculo: ", precios[i]) 
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")