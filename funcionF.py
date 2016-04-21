def superficie_Cono(a,b):
	import math
	pi = 3.141592653589793
	areaLateral = pi * a * b
	areaTotal = areaLateral + (pi * a**2)
	return areaTotal