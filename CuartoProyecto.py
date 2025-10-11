# Juego de Adivina el numero
from random import randint



def jugar():
     
    
    numeroUsuario = (int(input("Dame un numero entre 0 y 100: ")))

    if 0 <= numeroUsuario <= 100:
        numeroRandom = intento
    else:
        print("El numero no es valido")


    numeroRandom = randint(0, 100)


    if numeroRandom == intento:
        print("Ganaste!")
        print(f"El numero era {intento}.")
    
    else: 
        print("No Ganaste!")
        
for intento in range(8):
    if jugar():
        break
else:
    print("Lo siento, te quedaste sin oportunidades")
            