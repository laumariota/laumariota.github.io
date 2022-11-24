#app que al ingresar el valor que compra 
#si el valor de la compra es mayor a 100,000 pesos
#entonces calcule el descuento(7%) y el total de la compra

valor_compra=float(input("Digite el valor de la compra:"))
if valor_compra>100000:
    descuento=valor_compra*0.07
    total=valor_compra-descuento
    print("subtotal: ", valor_compra)
    print("descuento: ", descuento)
    print("total de la compra: ", total)
else:
    descuento=valor_compra*0.0
    total=valor_compra-descuento
    print("subtotal: ", valor_compra)
    print("descuento: ", descuento)
    print("total de la compra: ", total)