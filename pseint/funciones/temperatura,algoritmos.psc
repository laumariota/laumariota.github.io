SubProceso fiebre ( temp )
	Si temp>=38 Entonces
		escribir " el paciente tiene fiebre ";
	SiNo
		escribir "el paciente no tiene fiebre ";
	FinSi
	
FinSubProceso



Proceso temperatura
	definir temp como entero;
	escribir "por favor digite la temperatura del paciente";
	leer temp;
	fiebre(temp);
FinProceso
