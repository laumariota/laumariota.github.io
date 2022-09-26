//app para evaluar si un numero es positivo o es negativo
var n;
//capturando una entrada
n=parseInt(prompt("por favor digite un numero entero: "));
//evaluamos el proceso numerico
if (n>=0) {
    document.write("el numero " +n+ " es positivo  <img src='img/aceptar.png' height='24px'> ");
} else {
    document.write("el numero " +n+ " es negativo   <img src='img/cancelar.png' height='24px'> ");
}