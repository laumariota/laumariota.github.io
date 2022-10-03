//Funcion que suma de 2 numeros
function sumar(){
    var x,y, sumar
    
    
    x=parseInt(document.getElementById ("n1").value)
    y=parseInt(document.getElementById ("n2").value)
    
    sumar=x+y
    document.getElementById("resultado_sumar").innerHTML="el resultado de la suma es: "+sumar
}
//Funcion que suma de 2 numeros
function restar(){
    var x,y, restar
    
    
    x=parseInt(document.getElementById ("n1").value)
    y=parseInt(document.getElementById ("n2").value)
    
    restar=x-y
    document.getElementById("resultado_restar").innerHTML="el resultado de la resta es: "+restar
}
//Funcion que suma de 2 numeros
function multiplicar(){
    var x,y, multiplicar
    
    
    x=parseInt(document.getElementById ("n1").value)
    y=parseInt(document.getElementById ("n2").value)
    
    multiplicar=x*y
    document.getElementById("resultado_multiplicar").innerHTML="el resultado de mutiplicacion es: "+multiplicar
}
//Funcion que suma de 2 numeros
function dividir(){
    var x,y, dividir
    
    
    x=parseFloat(document.getElementById ("n1").value)
    y=parseFloat(document.getElementById ("n2").value)
    
    dividir=x/y
    document.getElementById("resultado_dividir").innerHTML="el resultado de la divicion es: "+dividir
}