# 7) Crear un programa que use el operador condicional para mostrar un el valor absoluto de un número
# de la siguiente forma: si el número es positivo, se mostrará tal cual; si es negativo, se mostrará
# cambiado de signo.

# funcion que multiplique el numero por -1 si es un numero negativo
# para que despues por ley de los signos cambie a positivo

usr_number = int(input('Ingrese numero a convertir a su valor absoluto: '))


def absolute_value_negatives_converter():
    if usr_number < 0:
        converter_to_absolute_value = usr_number * -1
        print(f'El valor absoluto de {usr_number} es {converter_to_absolute_value}')
    else:
        print(f'El valor absoluto de {usr_number} es {usr_number}')


if __name__ == '__main__':
    absolute_value_negatives_converter()
