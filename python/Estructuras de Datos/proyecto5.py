#for: recorrer una lista de colores
colores = ['0.amarillo', '1.azul', '2.rojo', '3.negro', '4.blanco', '5.plateado', '6.morado','7.rosado', '8.dorado']
#añadimos un elemento a la lista
colores.append('AZUL')
colores.remove("8.dorado")
#recorremos a la lista
for x in colores:
    print (x)
#definimos un elemento a la lista
longitud = len(colores)
print("el tamaño o longitud es: ", longitud)    