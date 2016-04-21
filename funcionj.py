# -*- coding: utf-8 -*-
def sumaImpares(a, b):
	if a % 2 != 0 and b % 2 != 0:
		suma = a + b
		print "La suma de ", a, " y ", b, " es ", suma
		return
	else:
		print "Los numeros ", a, b, " no son impares"
		return