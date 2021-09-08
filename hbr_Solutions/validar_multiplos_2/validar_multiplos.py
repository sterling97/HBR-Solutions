# 2) Crear un programa que pida al usuario dos números enteros y diga si el primero es múltiplo del
# segundo (pista: igual que antes, habrá que ver si el resto de la división es cero: a % b == 0).

urs_number = int(input('Digite el primer numero: '))
urs_number2 = int(input('Digite el segundo numero: '))


def validate_multiple():
    division = urs_number / urs_number2
    residue = urs_number % urs_number2
    if residue == 0:
        print(f'{urs_number} es multiplo de {urs_number2}')
    else:
        print(f'{urs_number} no es multiplo de {urs_number2}')


if __name__ == '__main__':
    validate_multiple()