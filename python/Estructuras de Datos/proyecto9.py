#recorrer una lista vacia de que almacene los datos de un sistema de facturación
factura=[]
cliente=[]
nombre=[]
fecha=[]
producto=[]
unitario=[]
cantidad=[]
totales=[]
#se define un tamaño para la lista del vehiculo
tamaño=int(input("tamaño de lista de un sistema de facturacion: "))
#se recorre la lista del tamaño definido
for i in range(tamaño): 
    print("ingrese los datos de la factura del cliente: ", i+1)
    facturas=input("el codigo de la factura es: ")
    clientes=input("el codigo del cliente es: ")
    nombres=input("nombre del cliente: ")
    fechas=input("fecha de su factura: ")
    productos=input("descripcion del producto: ")
    unitarios=int(input("precio unitario: "))
    cantidads=int(input("cantidad: "))  
    factura.append(facturas)
    cliente.append(clientes)
    nombre.append(nombres)
    fecha.append(fechas)
    producto.append(productos)
    unitario.append(unitarios)
    cantidad.append(cantidads)
    totales.append(cantidads*unitarios)
print("Informacion de la factura: ")
for i in range(tamaño):
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("el codigo de la factura es:", factura[i]) 
    print("----------------------------------------------")
    print("el codigo del cliente es: ",cliente[i])
    print("----------------------------------------------")
    print("nombre del cliente: ",nombre[i])
    print("----------------------------------------------")
    print("fecha de su factura: ", fecha[i])
    print("----------------------------------------------")
    print("descripcion del producto: ",producto[i])  
    print("----------------------------------------------")  
    print("precio unitario: ", unitario[i]) 
    print("----------------------------------------------")
    print("cantidad: ",cantidad[i])  
    print("----------------------------------------------")  
    print("totalidad de su facturcion: ",totales[i]) 
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

