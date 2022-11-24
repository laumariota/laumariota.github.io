#for: recorrer una listas de lenguaje de programacion
lenguaje = ['0.javascrip', '1.python', '2.java', '3.php', '4.objetive-c', '5.c/c++']
#añadimos un elemento a la lista
lenguaje.append('DELPHI')
lenguaje.pop(4)
#recorremos a la lista
for x in lenguaje:
    print(x)
#definimos un elemento a la lista
longitud = len(lenguaje)
print("el tamaño o longitud es: ", longitud)