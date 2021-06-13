# Importar random
import random

# Funcion guess
def computer_guess(x):
    low = 1
    high = x
    feed = ''
    while feed != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feed = input(f'Es {guess} demasiado grande (G), demasiado pequeño (P) o correcto (C)??').lower()
        if feed == 'g':
            high = guess - 1
        elif feed == 'p':
            high = guess + 1
    
    print(f'La computadora adivino tu numero {guess} correctamente!!')

computer_guess(10)