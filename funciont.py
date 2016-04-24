# -*- coding: utf-8 -*-

print "### FuncionT ###"
def billetes (monto):
	a, b, c, d, e, f, g= 1, 2, 5, 10, 20, 50, 100
	flag = True
	rest = monto
	cont1, cont2, cont5, cont10, cont20, cont50, cont100 = 0, 0, 0, 0, 0, 0, 0

	while flag:
		if rest >= 100:
			rest=rest - 100
			cont100 += 1
		elif rest >= 50:
			rest=rest - 50
			cont50 += 1
		elif rest >= 20:
			rest=rest - 20
			cont20 += 1
		elif rest >= 10:
			rest=rest - 10
			cont10 += 1
		elif rest >= 20:
			rest=rest - 10
			cont10 += 1
		elif rest >= 5:
			rest=rest - 5
			cont5 += 1
		elif rest >= 2:
			rest=rest - 2
			cont2 += 1
		elif rest >= 1:
			rest=rest - 1
			cont1 += 1
		else:
			flag = False
	print cont1, cont2, cont5, cont10, cont20, cont50, cont100
	if cont1 != 0:
		print "Necesita", cont1, "monedas de 1 peso"
	if cont2 != 0:
		print "Necesita", cont2, "billetes de 2 pesos"
	if cont5 != 0:
		print "Necesita", cont5, "billetes de 5 pesos"
	if cont10 != 0:
		print "Necesita", cont10, "billetes de 10 pesos"
	if cont20 != 0:
		print "Necesita", cont20, "billetes de 20 pesos"
	if cont50 != 0:
		print "Necesita", cont50, "billetes de 50 pesos"
	if cont100 != 0:
		print "Necesita", cont100, "billetes de 100 pesos"

monto = input ("ingrese un monto: ")
billetes (monto)