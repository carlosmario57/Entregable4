import random

numero_secreto = random.randint(1, 10)
adivina = 0

while adivina != numero_secreto:
    adivina = int(input("Adivina el número entre 1 y 10: "))
    if adivina < numero_secreto:
        print("Es mayor")
    elif adivina > numero_secreto:
        print("Es menor")

print("¡Correcto! El número era", numero_secreto)
