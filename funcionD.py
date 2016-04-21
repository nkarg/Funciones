print "## D ##"
def potencia(j,h):
	prod=1
	for i in range (h):
		prod = prod * j
	print ("Base",j,"exponente",h ,"=",prod)
print " Ingrese dos numeros naturales j y h e imprima j elevado a la h utilizando solo la operacion multiplicacion."
x = input("Ingrese la base: ")
y= input("Ingrese el exponente: ")
potencia(x,y)
