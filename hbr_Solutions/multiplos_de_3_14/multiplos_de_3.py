# 14) Crear un programa que escriba en pantalla los números del 1 al 50 que sean múltiplos de 3 (pista:
# habrá que recorrer todos esos números y ver si el resto de la división entre 3 resulta 0).

number = 0

while number < 50:
    number += 1
    if number % 3 == 0:
        print(number)
