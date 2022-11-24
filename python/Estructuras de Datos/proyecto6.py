#recorremos las listas (vacias al comienzo)
nombres=[]
fecha=[]
lugar=[]
identificacion=[]
correo=[]
telefono=[]
direccion=[]
#definimos un tamaño para la lista
tamaño=int(input("tamaño de la lista?: "))
#recorremo la lista del tamaño definido
for i in range(tamaño):
    print("ingrese los datos del aprendiz: ", i+1)
    nombre=input("Nombre del Aprendiz: ")
    fch=input("Fecha de Nacimiento: ")
    lugars=input("Lugar de Nacimiento: ")
    id=input("N° de Identificacion: ")
    C=input("Correo Electronico: ")
    tel=input("N° de Telefono: ")
    drc=input("Direccion: ")
    nombres.append(nombre)
    fecha.append(fch)
    lugar.append(lugars)
    identificacion.append(id)
    correo.append(C)
    telefono.append(tel)
    direccion.append(drc)
print("informacion del aprendiz: ")
 #ahora mostremos la listas
for i in range (tamaño):
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("nombre:", nombres[i]) 
    print("--------------------------------------")
    print("Fecha de Nacimiento: ",fecha[i])
    print("--------------------------------------")
    print("Lugar de Nacimiento: ",lugar[i])
    print("--------------------------------------")
    print("Identificacion: ", identificacion[i])
    print("--------------------------------------")
    print("Correo Electronico: ",correo[i])  
    print("--------------------------------------")  
    print("N° de Telefono: ", telefono[i]) 
    print("--------------------------------------")
    print("Direccion: ",direccion[i])
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°|")