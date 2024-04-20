import math
import random

lower = int(input("ingrese un número inferior: "))
upper = int(input("ingrese un número superior: "))

# Generando un numero aleatorio entre lower y upper
x = random.randint(lower, upper)
print("\nSolo tienes",
      round(math.log(upper - lower + 1, 2)),
      "oportunidades para adivinar! \n"
      )

# Inicio del número de adivinanzas
count = 0

# Para calcular el minimo de número de adivinanzas
while count < math.log(upper - lower + 1, 2):
    count += 1
    adivina = int(input("adivina un número: "))

    # Prueba de la condición
    if x == adivina:
        print("felicidades lo lograste en",
              count, " intentos")

        # Una vez adivinado se rompe el bucle
        break

        # sino hacemos un if
    elif x > adivina:
        print("adivinaste muy bajo!!")
    elif x < adivina:
        print("adivinaste muy alto!!")

# Si las adivinanzas son mas de las requeridas
# muestra este resultado
if count >= math.log(upper - lower + 1, 2):
    print("\n el número es %d" % x)
    print("\tMejor suerte en la proxima!!!")
