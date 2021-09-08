# 4) Crear un programa que pida al usuario dos números reales. Si el segundo no es cero, mostrará el
# resultado de dividir entre el primero y el segundo. Por el contrario, si el segundo número es cero,
# escribirá “Error: No se puede dividir entre cero”

urs_number = int(input('Digite el primer numero: '))
urs_number2 = int(input('Digite el segundo numero: '))

while urs_number2 == 0:
    print('Error: No se puede dividir entre cero')
    urs_number2 = int(input('Digite el primer numero: '))


divide = urs_number / urs_number2


print(f'El resultado es: {divide}')