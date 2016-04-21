print "## C ##"
def mostrarParImpar(a):
	if a%2 ==0:
		for i in range(a+1):
			if i%2==0:
				print i
	else:
		for i in range(a+1):
			if i%2==1:
				print i
print "Dado un numero natural m, si es par imprime los m primeros naturales pares y si es impar a la inversa\n"
x = input("Ingrese un Numero: ")
mostrarParImpar(x)
