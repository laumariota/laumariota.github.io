#1.Diseñe una app que permita al usuario ingresar nombre, edad, dirección y teléfono; 
#estos datos se deben almacenar en un diccionario llamado persona. 
#Estos datos se deben mostrar por pantalla de forma concatenado. 
#EJEMPLO: juan tiene 17 años vive en la calle 8 N°27-8ª y su número de teléfono es 123456789
nombre=input("Digite su nombre: ")
edad=input("digite su edad: ")
direccion=input("digite su direccion: ")
telefono=input("digite su telefono: ")

persona={"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}
print(persona["nombre"], "tiene: ", persona["edad"], "años",", y vive en: ", persona["direccion"], "y su numero de telefono es: ", persona["telefono"])
 
