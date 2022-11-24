#recorrer una lista vacia de una tienda de peliculas
titulos=[]
generos=[]
duracion=[]
protagonistas=[]
año=[]
precios=[]
idiomas=[]
#se define un tamaño para la lista de peliculas
tamaño=int(input("tamaño de la tienda de peliculas: "))
#se recorre una lista de tamaño definido
for i in range(tamaño):
    print("por favor ingrese los datos de la tienda de peliculas: ", i+1)
    titulo=input(" titulo de la pelicula: ")
    genero=input("genero de la pelicula: ")
    drcn=input("duracion de la pelicula: ")
    protagonista=input("protagonista de la pelicula: ")
    años=input("año de estreno de la pelicula: ")
    precio=input("cual es el precio de la pelicula: ")
    idioma=input("idiomas de la peliculas: ")
    titulos.append(titulo)
    generos.append(genero)
    duracion.append(drcn)
    protagonistas.append(protagonista)
    año.append(años)
    precios.append(precio)
    idiomas.append(idioma)
print("Informacion del vehiculo: ")
for i in range(tamaño):
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print(" titulo de la pelicula:", titulos[i]) 
    print("-----------------------------------------------")
    print("genero de la pelicula: ",generos[i])
    print("-----------------------------------------------")
    print("duracion de la pelicula: ",duracion[i])
    print("-----------------------------------------------")
    print("protagonista de la pelicula: ", protagonistas[i])
    print("-----------------------------------------------")
    print("año de estreno de la pelicula: ",año[i])  
    print("-----------------------------------------------")  
    print("cual es el precio de la pelicula: ", precios[i])
    print("-----------------------------------------------")  
    print("idiomas de la peliculas: ", idiomas[i]) 
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")