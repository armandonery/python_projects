# Importar random
import random

# Funcion guess
def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Adivina el numero entre 1 y {x}:"))
        if guess < random_num:
            print('Lo siento, es demasido pequeño, intenta de nuevo.')
        elif guess > random_num:
            print('Lo siento, es demasiado grande, intenta de nuevo.')
                
    print(f'Correacto, adivinaste el numero {random_num}!!')

guess(10)