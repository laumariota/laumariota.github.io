var a,b
var i
a=parseInt(prompt("por favor ingrese el valor inicial: "))
b=parseInt(prompt("por favor ingrese el valor final: "))
for(i=a; i<=b; i++)
    if (i%2==0) {
    document.write(i) 
   }
   else(
       document.write("<br>")
   )