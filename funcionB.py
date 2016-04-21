print "## B ##"
def sumaPrimerosN(a):
	sum = 0
	for i in range(1,a+1):
		sum +=i
	print("La suma de los primeros",a,"numeros es:",sum)
print "Dado un numero natural n, calcule la suma de los n primeros numeros naturales\n"
x= input("Ingrese un Numero: ")
sumaPrimerosN(x)
