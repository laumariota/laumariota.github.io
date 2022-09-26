//app para evaluar un numero entre 10 y 100
var n;
//capturando una entrada
n=parseInt(prompt("por favor digite un numero entero: "));
//evaluamos el proceso numerico
if (n>10 && n<=100) {
    document.write("el numero " +n+ " esta entre 10 y 100 ");
} else {
    document.write("el numero " +n+ " no esta entre 10 y 100 ");
}