"""valor por declarar
=<100.000.000 tiene el 5%
100.000.000>=200.000.000 tiene el 15%
200.000.000>=350.000.000 tiene el 20%
350.000.000>=600.000.000 tiene el 30%
600.000.000>= tiene el 45%
"""

renta=int(input("Ingrese el valor por declarar: "))
impuesto=float(input("Ingrese el impuesto: "))
operacion=renta*impuesto

if impuesto<100000000:
    descuento=operacion*0.05
    print("El usuario obtuvo un descuento de 05% que es $", descuento, " sobre el total de la renta ")
    total=operacion-descuento
    print("El el valor del usuario es de: $", total)
elif impuesto>=100000000 and impuesto<200000000:
    descuento=operacion*0.15
    print("El usuario obtuvo un descuento de 15% que es $", descuento, " sobre el total de la renta ")
    total=operacion-descuento
    print("El el valor del usuario es de: $", total)
elif impuesto>=200000000 and impuesto<350000000:
    descuento=operacion*0.20
    print("El cliente obtuvo un descuento de 20% que es $", descuento, " sobre el total de la renta")
    total=operacion-descuento
    print("El el valor del usuario es de: $", total)
elif impuesto>=350000000 and impuesto<600000000:
    descuento=operacion*0.30
    print("El cliente obtuvo un descuento de 30% que es $", descuento, " sobre el total de la renta")
    total=operacion-descuento
    print("El el valor del usuario es de: $", total)
elif impuesto>=600000000:
    descuento=operacion*0.45
    print("El cliente obtuvo un decuento de 45% que es $", descuento, " sobre el total de la  renta")
    total=operacion-descuento
    print("El el valor del usuario es de: $", total)
else:
    print("Ingrese una cantidad valida")
