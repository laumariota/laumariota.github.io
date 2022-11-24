#Algoritmo que ofrese 15% de descuento de una cuenta
compra=float(input("Ingrese el valor de la compra: "))
descuento=compra*0.15
total=compra-descuento
print("El 15% de descuento es",descuento,". El cliente debe pagar un total de",total)