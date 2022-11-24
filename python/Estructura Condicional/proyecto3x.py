"""Evaluar la siguiente tabla
<=18.5, bajo peso
18.5>= y <24.9, normal
25>= y <29.9, sobre peso
30>= y <34.9, obesidad I
35>= y <39.9, obesidad II
40>= y <49.9, obesidad III
>=50 obesidad IV
"""
imc=float(input("ingrese su peso: "))
if  imc<18.5:
    print("bajo de peso")
elif imc>=18.5 and imc<24.9:
    print("normal")
elif imc>=25 and imc<29.9:
    print("sobre peso")
elif imc>=30 and imc<34.9:
    print("obesidad I")
elif imc>=35 and imc<39.9:
    print("obesidad II")
elif imc>=40 and imc<49.9:
    print("obesidad III")
elif imc>=50:
    print("obesidad IV")
    print("... por favor verifique!")