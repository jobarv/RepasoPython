# Crea un programa que le informe al vendedor cuanto es el monto de comision que obtiene al final del mes.

# Pregunta al usuario su nombre y cuanto vendio
nombre = input("Cual es tu nombre?: ")
ventas = float(input("Cual fueron las ventas de este mes?: "))

# Calcula la comision del 13% sobre las ventas
comision = ventas * 0.13
comision = round(comision,2)

# Informale al usuario su comision
print(f"Hola {nombre}, tu comision es de: $ {comision}")