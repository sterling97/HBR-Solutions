# 1) El usuario tecleará dos números (x e y), y el programa deberá calcular cual es el resultado de su
# división y el resto de esa división.

urs_number = int(input('Digite el primer numero: '))
urs_number2 = int(input('Digite el segundo numero: '))


def operator():
    division = urs_number / urs_number2
    residue = urs_number % urs_number2
    print(f'El resultado de la division es: {division}')
    print(f'El reciduo de la operacion es: {residue}')


if __name__ == '__main__':
    operator()