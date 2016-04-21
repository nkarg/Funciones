# -*- coding: utf-8 -*-
def tipoNum(n):
	if n <= 0:
		print "Error ", n, " no es un numero natural"
	else:
		cant = 0
		resp = ""
		print "El numero ", n, " tiene como divisores a: "
		for i in range(1, n+1):
			if n % i == 0:
				resp = resp + str(i) + "-"
				cant = cant + i
		print resp	
		if cant == n:
			print " La suma es:", cant, "El numero es Perfecto"
			return
		elif cant < n:
			print " La suma es:", cant, "El numero es Deficiente"
			return
		else:
			print "La suma es:", cant, "El numero es abundante"
			return