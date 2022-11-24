"""Evaluar la grafica de presion aterial
<=90, baja
90>= y <120, normal
120>= y <139, prehipertencion
140>= y <159, alta prehipertencion fase 1
>=160 alta prehipertencion fase 2
"""
presion_arterial=int(input("ingrese su presion: "))
if  presion_arterial<90:
    print("baja de presion")
elif presion_arterial>=90 and presion_arterial<120:
    print("presion normal ")
elif presion_arterial>=120 and presion_arterial<139:
    print("presion prehipertencion")
elif presion_arterial>=140 and presion_arterial<159:
    print("presion alta prehipertencion fase 1")
elif presion_arterial>=160:
    print("presion alta prehipertencion fase 2")
    print("... por favor verifique su presion!")