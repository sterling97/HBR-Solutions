# 3) Crear un programa que multiplique dos números enteros de la siguiente forma: pedirá al usuario un
# primer número entero. Si el número que se que teclee es 0, escribirá en pantalla "El producto de 0 por
# cualquier número es 0". Si se ha tecleado un número distinto de cero, se pedirá al usuario un segundo
# número y se mostrará el producto de ambos.


urs_number = int(input('Digite el primer numero: '))


while urs_number == 0:
    print('El producto de 0 por cualquier número es 0')
    urs_number = int(input('Digite el primer numero: '))


urs_number2 = int(input('Digite el segundo numero: '))
multiplate = urs_number * urs_number2


print(f'El resultado es: {multiplate}')

