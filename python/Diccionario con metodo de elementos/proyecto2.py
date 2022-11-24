#2.Diseñe una app que permita al usuario ingresar fruta, el precio unitario y la cantidad
#lo almacene en un diccionario llamado factura. Después debe mostrar un mensaje concatenado
#donde aparece el nombre de la fruta su valor la cantidad y el total.
fruta=input("Digite la fruta: ")
precio=int(input("Digite el valor de la fruta: "))
cantidad=int(input("que cantidad desea llevar: "))
total=precio*cantidad
factura={"fruta":fruta, "cantidad":cantidad,"precio":precio, "total":total}
print(factura["fruta"], "esta fruta tiene un valor de: ", factura["precio"],"pesos y su cantidad deseada al llevar es de: ", factura["cantidad"], "y tiene un valor de: ", factura["total"], "pesos")


