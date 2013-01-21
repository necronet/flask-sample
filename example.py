from random import randint

#Randint(a,b) crea un valor entre a y b aleatorio
a = randint(1,500)
b = randint(1,1000)
resultado = b - a


if resultado > 0:
	resultado_cadena= 'El resultado es mayor a 0 %d'
	if resultado > 100:
		resultado_cadena= "Mayor a 100 %d"
	else:
		resultado_cadena= "Naaa es menor que 100 %d"
else:
	resultado_cadena= 'Ya ahora el resultado es menor que 0 %d'

print resultado_cadena % resultado

