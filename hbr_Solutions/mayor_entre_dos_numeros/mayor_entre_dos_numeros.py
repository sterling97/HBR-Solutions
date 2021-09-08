

usr_number = int(input("Numero 1: "))
usr_number2 = int(input("Numero 2: "))


def decide():
    if usr_number == usr_number2:
        print(f"{usr_number} es igual a {usr_number2}")
    elif usr_number > usr_number2:
        print(f"{usr_number} es mayor a {usr_number2}")
    else:
        print(f"{usr_number} es menor a {usr_number2}")


def another_way():
    print('Otra Manera')
    if (usr_number > usr_number2):
        valor = "MAYOR"
        print(f'{usr_number} es {valor} que {usr_number2}')
    elif (usr_number == usr_number2):
        valor = "IGUAL"
        print(f'{usr_number} es {valor} que {usr_number2}')
    else:
        valor = "MENOR"
        print(f'{usr_number} es {valor} que {usr_number2}')


if __name__ == '__main__':
    decide()
    another_way()