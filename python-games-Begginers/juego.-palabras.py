import random

nombre = input("Cual es tu nombre: ")
print("Buena Suerte!", nombre)

palabras = ['flowers', 'roses', 'yellow', 'rainbow', 'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

palabra = random.choice(palabras)
print("\nadivina las letras de la palabra")

adivinando = ''
intentos = 10
fallos = 0

while intentos > 0:
    if fallos >= 10:
        print("Perdiste")
        break

    for char in palabra:
        if char in adivinando:
            print(char, end="")
        else:
            print("_", end="")

    if all(char in adivinando for char in palabra):
        print("\n¡Ganaste!")
        print("La palabra es:", palabra)
        break

    adivina = input("\nAdivina una letra: ")
    adivinando += adivina

    if adivina not in palabra:
        fallos += 1
        print("Incorrecto")
        print("Tienes", fallos, "intentos más.")




