import math

radio = int(input("ingrese el radio de un circulo: "))
area = math.pi * radio**2
perimetro = 2*math.pi *radio
mensaje = f"la area del circulo es igual a: {area}. el perimetro del circulo es igual a: {perimetro}"
print(mensaje)
