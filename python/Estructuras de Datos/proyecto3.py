#for: recorrer una lista de plantas medicinales
planta =['0.flor de sauco', '1.estragon', '2.jazmin', '3.melisa','4.aloe vera','5.apio','6.manzanilla', '7.oregano','8.ajo', '9.eucalipto']
#añadimos un elemento a la lista
planta.append('EL ROMERO')
planta.remove("2.jazmin")
#recorremos a la lista
for x in planta:
    print (x)
#definimos un elemento a la lista
longitud = len(planta)
print("el tamaño o longitud es: ", longitud)    