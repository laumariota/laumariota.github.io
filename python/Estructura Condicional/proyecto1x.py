"""Evaluar la edad ingresada
0>= y <2, Eres un Baby
2>= y <12, Eres un Niño(a)
12>= y <17, Eres un Adolecente
18>= y <40, Eres un Adulto joven
40>= y <60, Eres un Adulto maduro
>=60 Eres un Adulto Mayor
"""
edad=int(input("ingrese la edad: "))
if edad>=0 and edad<2:
    print("Eres un baby")
elif edad>=2 and edad<12:
    print("Eres un niño(a)")
elif edad>=12 and edad<18:
    print("Eres un Adolecente")
elif edad>=18 and edad<40:
    print("Eres un Adulto joven")
elif edad>=40 and edad<60:
    print("Eres un Adulto maduro")
elif edad>=60:
    print("Eres un Adulto mayor")
    print("esto no es una edad... por favor verifique!")
