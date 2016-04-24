# -*- coding: utf-8 -*-

print "### Funcion S ###"

def Edades (a, b):
	if a > b:
		print "La Primera Edad ingresada es mayor a la segunda ingresada"
		anio = a - b
		print "Le falta",anio, "anios para alcanzar a la primera Edad"
	else:
		print "La Segunda Edad ingresada es mayor a la primera ingresada"
		anio1 = b - a 
		print "Le falta",anio1, "anios para alcanzar a la segunda edad"

a = input ("Ingrese Primera Edad: ")
b = input ("Ingrese Segunda Edad: ")

Edades (a, b)