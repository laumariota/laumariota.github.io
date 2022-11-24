#diseñe una app que permita almacenar la informacion de los clientes de una empresa.
#los clientes se guardaran en un diccionario llamado clientes.los datos deben ser ingresado por el usuario;
#identificacion del cliente, nombre, direccion, telefono, correo y empresa. 
#la app debe preguntar al usuaro por una opcion del menu.
#1.añadir cliente 2.mostrar cliente 3.eliminar cliente 4.salir
clientes={}
op=""
while op !=4:
    if op ==1:
        identificacion=input("Digite su identificacion: ")
        nombre=input("escriba su nombre: ")
        direccion=input("Escriba su direccion: ")
        telefono=input("Digite su numero de telefono: ")
        correo=input("Escriba su correo electronico: ")
        empresa=input("Escriba el nombre de su empresa: ")
        cliente={
        "identificacion":identificacion,
        "nombre":nombre,
        "direccion":direccion,
        "telefono":telefono,
        "correo":correo,
        "empresa":empresa}
    if op ==2:
        print("°°Informacion del Cliente°°")
        print("---------------------------")
        print("identificacion: " , cliente["identificacion"])
        print("nomdre: " , cliente["nombre"])
        print("direccion: " , cliente["telefono"])
        print("correo: " , cliente["correo"])
        print("empresa: " , cliente["empresa"])
        print("-----------------------------")
    if op ==3:
        del cliente["identificacion"]
    if op ==4:
       exit()
 
    print("°°°°°°°MENU°°°°°°°")
    print("1- AÑADIR CLIENTE")
    print("2- MOSTRAR CLIENTE")
    print("3- ELIMINAR CLIENTE")
    print("4- SALIR")
    op=int(input("Digite la opcion seleccionada: "))
