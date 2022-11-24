#FUNCIONES CON PARAMETROS
#Escribir una funcion a la que 
#se le pase una cadena <nombres> y 
#muestre por pantalla el saludo 
#¡hola <nombres>!

def saludo(name):
    print("hola", name)

#app que ingrese el nombre y lo muetre como saludo
nombre=input("¿ Cual es tu nombre ?")

saludo(nombre) #llamando a la funcion