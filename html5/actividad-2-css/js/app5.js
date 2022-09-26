//app para evaluar si es mayor de edad o menor de edad
var n;
//capturando una entrada
n=parseInt(prompt("por favor digite una edad: "));
//evaluamos el proceso numerico
if (n>=18) {
    document.write( +n+" eres mayor de edad <img src='img/plus-18-pelicula.png' height='24px'>" );
} else {
    document.write( +n+ " eres menor de edad <img src='img/no-menores.png' height='24px'> ");
}