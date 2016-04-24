# -*- coding: utf-8 -*-

print "### Funcion Q ###"

def funcion (a, b):
	if a == len(b):
		print (" La palabra tiene la misma cantidad de caracteres que el numero ingresado")
	else:
		print ("La palabra no tiene la misma cantidad de caracteres que el numero ingresado")

a = input ("ingrese un Numero: ")
b = raw_input ("ingrese una palabra: ")

funcion (a, b)