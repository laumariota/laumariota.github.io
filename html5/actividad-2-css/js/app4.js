//app para evaluar una nota
var n;
//capturando una entrada
n=parseFloat(prompt("por favor digite una nota: "));
//evaluamos el proceso numerico
if (n>=3.0) {
    document.write("su nota " +n+ " es aprobada ");
} else {
    document.write("su nota " +n+ " es reprobada");
}