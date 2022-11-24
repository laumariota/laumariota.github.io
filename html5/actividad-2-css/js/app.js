//Aplicacion para evaluar la fiebre de una persona
var temp;

//Capturar los datos de entrada
temp=parseFloat(prompt("ingrese su temperatura en °c: "));


//proceso para evaluar la fiebre
if (temp>=38) {
  document.write(" la temperatura " +temp+ "°c indica fiebre <img src='img/calor.png' height='24px'> "  ) ; 
} else {
  document.write(" la temperatura " +temp+ "°c indica paciente sin fiebre"); 
}