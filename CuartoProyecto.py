# Juego de Adivina el numero
from random import randint

for intento in range(8):

    numeroUsuario = (int(input("Dame un numero entre 0 y 100: ")))

    if 0 <= numeroUsuario <= 100:
    
        numeroRandom = randint(0, 100)

    else:
        print("El numero no es valido")

    if numeroRandom == numeroUsuario:
        print("Ganaste!")
        print(f"El numero era {numeroRandom}.")
    
    else: 
        print("No Ganaste!")
        
else:
    print("Lo siento, te quedaste sin oportunidades.")
    print(f"El numero era: {numeroRandom}")
    