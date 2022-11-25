SubProceso  par ( n )
	Si (n mod 2)=0 Entonces
		escribir " el numero es ", n, " es par ";
	SiNo
		escribir " el numero es ", n, " es impar ";
	FinSi
	
FinSubProceso

Proceso par_o_impar 
	Definir n Como entero;
	escribir "por favor digite el el numero: ";
	leer n;

	par( n );
FinProceso
