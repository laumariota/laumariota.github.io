#for: recorrer una lista de libros 
libros = ['0.el principito', '1.el zoo humano', '2.momo', '3.la peste', '4.el extranjero', '5.el lector', '6.soy leyenda', '7.novela de ajedrez']
#añadimos un elemento a la lista
libros.append('LA BESTIA')
libros.pop(1)
#recorremos a la lista
for x in libros:
    print (x)
#definimos un elemento a la lista
longitud = len(libros)
print("el tamaño o longitud es: ", longitud)