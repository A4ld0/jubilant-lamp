#Esta libreria se usa para generar numeros random para el funcionamiento del juego
import random

#Funcion para iniciar el juego
def start_game():
    """
    Inicia un juego donde el usuario debe adivinar un número aleatorio entre 1 y 20.
    Y te va diciendo si estas muy bajo o muy alto y te va contando los intentos.
    """

    number = random.randint(1, 20)
    guess = 0
    attempts = 0

    print("Adivina el número entre 1 y 20")

    # Solicitar el límite de intentos
    while True:
        try:
            max_attempts = int(input("¿Cuantos intentos quieres tener?: "))
            if max_attempts > 0:
                break
            else:
                print("Por favor, ingresa un numero positivo.")
        except ValueError:
            print("Error: debes ingresar un número valido.")

    while guess != number and attempts < max_attempts:
        try:
            guess = int(input("Ingresa tu intento: "))
            attempts += 1

            if guess < number:
                print("Muy bajo")
            elif guess > number:
                print("Muy alto")
            else:
                print("Adivinaste el número.")
                print(f"Lo lograste en {attempts} intentos.")
                break

            if attempts < max_attempts:
                print(f"Te quedan {max_attempts - attempts} intento(s).")
            else:
                print("Se te acabaron los intentos.")
                print(f"El numero correcto era {number}.")

        except ValueError:
            print("Error: debes ingresar un numero valido.")

start_game()
