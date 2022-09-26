//Defino las variables
var perimetro, lado1, lado2;
//capturar los datos del usuario
lado1=parseFloat(prompt("ingrese el lado 1 del triangulo: "));
lado2=parseFloat(prompt("ingrese el lado 2 del triangulo: "));
 
//proceso de la multiplicacion
perimetro=(lado1*lado2)/2;
//mensaje que se muestra en la consola
//console.log("el perimetro del triangulo es: "+perimetro);
//mensahe de salida
document.write("el perimetro del triangulo es:" +perimetro);
//mensaje de alerta
//alert("el perimetro del triangulo es: "+perimetro)