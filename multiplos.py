"""
Julieta Núñez Pacheco
19 de septiembre de 2025
Este ejercicio indica si un número es múltiplo de otro
"""

# Entradas
num1 = int(input("un numero: "))
num2 = int(input("otro numero: "))

# Proceso

if num1 % num2 == 0:
    multiplo = str(num1) + " es multiplo de " + str(num2)
elif num2 % num1 == 0:
    multiplo = str(num2) + " es multiplo de " + str(num1)
else: 
    multiplo = "Ninguno de los números es múltiplo del otro"


# Salidas
print(multiplo)
