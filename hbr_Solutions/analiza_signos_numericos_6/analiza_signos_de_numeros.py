# 6) Crear un programa que pida al usuario dos números enteros y diga "Uno de los números es positivo",
# "Los dos números son positivos" o bien "Ninguno de los números es positivo", según corresponda.

usr_number = int(input('Ingrese el primer digito: '))
usr_number2 = int(input('Ingrese el segundo digito: '))


def number_identifier():
    if usr_number < 0 and usr_number2 > 0:
        print('Uno de los números es positivo')
    elif usr_number > 0 and usr_number2 < 0:
        print('Uno de los números es positivo')
    elif usr_number and usr_number2 > 0:
        print('Los dos números son positivos')
    else:
        print('Ninguno de los números es positivo')


if __name__ == '__main__':
    number_identifier()