//Definimos variables
var peso, estatura, imc
//calculamos entrada
peso=parseFloat(prompt("por favor digite el peso en kg: "))
estatura=parseFloat(prompt("por favor digite la estatura en mts: "))
//calculamos proceso
imc=peso/(estatura*estatura)
//proceso-salida
if (imc<18.5) {
    document.write("bajo peso<img src='img/bajo-peso.png' with='20 px' height='20 px'>");
}else if(imc >=18.5 && imc <=24.9){
    document.write("peso normal<img src='img/peso normal.png' width='20 px' height='20 px'>")
}else if(imc >=25 && imc <=29.9){
    document.write("sobre peso<img src='img/sobre peso.png' width='20 px' height='20 px'>")
}else if(imc >=30 && imc <=34.9){
    document.write("obesidad I<img src='img/obesidad-I.png' width='20 px' height='20 px'>")
}else if(imc >=35 && imc <=39.9){
    document.write("obesidad II<img src='img/obesidad-II.png' width='20 px' height='20 px'>");
}else if(imc >=40 && imc <=49.9){
    document.write("obesidad III<img src='img/obesidad-III.png' width='20 px' height='20 px'>");
}else if(imc >=50){
    document.write("obesidad IV<img src='img/obesidad-IV.png' width='20 px' height='20 px'>");
}else{document.write("escriba los valores numericos esperados....")
}
