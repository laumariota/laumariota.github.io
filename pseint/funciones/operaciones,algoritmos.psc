SubProceso  sumar ( n1,n2 )
	Escribir " la suma de: ",n1, " + ",n2, " = ", n1+n2;
FinSubProceso
SubProceso  restar ( n1,n2 )
	Escribir " la resta de: ",n1, " - ",n2, " = ", n1-n2;
FinSubProceso
SubProceso  multiplicar ( n1,n2 )
	Escribir " la multiplicar de: ",n1, " * ",n2, " = ", n1*n2;
FinSubProceso
SubProceso  dividir ( n1,n2 )
	Escribir " la dividir de: ",n1, " / ",n2, " = ", n1/n2;
FinSubProceso

Proceso operaciones
	Definir a,b Como Entero;
	escribir "por favor digite el 1er numero: ";
	leer a;
	escribir "por favor digite el 1er numero: ";
	leer b;
	sumar(a,b);
	restar(a,b);
	multiplicar(a,b);
	dividir(a,b);
FinProceso
