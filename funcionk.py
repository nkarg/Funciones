# -*- coding: utf-8 -*-
def numH(n):
	if n <= 0:
		print "Error ", n, " no es un numero natural"
	else:
		suma = 0
		i = 1
		while i <= n:
			suma = suma + (suma + (1.0 / n))
			i= i + 1
		print suma
		return