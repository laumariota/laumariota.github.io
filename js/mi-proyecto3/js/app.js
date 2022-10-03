
var op;
var n1, n2, resultado;

op=parseInt(prompt("escoja una opcion: 1.suma 2.resta 3.multiplicacion 4.divison"))
switch (op) {
    case 1:
        n1=parseInt(prompt("digite el 1er numero"))
        n2=parseInt(prompt("digite el 2do numero"))
        resultado=n1+n2
        document.write("la suma de: "+n1+" + "+n2+" = "+resultado);
        break;
    case 2:
        n1=parseInt(prompt("digite el 1er numero"))
        n2=parseInt(prompt("digite el 2do numero"))
        resultado=n1-n2
        document.write("la resta de: "+n1+" - "+n2+" = "+resultado);
        break;
    case 3:
        n1=parseInt(prompt("digite el 1er numero"))
        n2=parseInt(prompt("digite el 2do numero"))
        resultado=n1*n2
        document.write("la multiplicacion de: "+n1+" * "+n2+" = "+resultado);
        break;
    case 4:
        n1=parseFloat(prompt("digite el 1er numero"))
        n2=parseFloat(prompt("digite el 2do numero"))
        resultado=n1/n2
        document.write("la division de: "+n1+" / "+n2+" = "+resultado);
        break;
    default:document.write("seleccione una opcion del menu");
        break;

}



