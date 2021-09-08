

usr_number = int(input("Numero 1: "))
usr_number2 = int(input("Numero 2: "))
usr_number3 = int(input("Numero 3: "))


def define_mayor_menor():
    if usr_number > usr_number2 and usr_number2 > usr_number3:
        print(f"""Mayor: {usr_number} 
Menor: {usr_number3}""")

    elif usr_number2 > usr_number and usr_number > usr_number3:
        print(f"""Mayor: {usr_number2} 
Menor: {usr_number3}""")

    elif usr_number3 > usr_number and usr_number > usr_number2:
        print(f"""Mayor: {usr_number3}
Menor: {usr_number2}""")

    elif usr_number3 > usr_number2 and usr_number2 > usr_number:
        print(f"""Mayor: {usr_number3} 
Menor: {usr_number}""")

    elif usr_number > usr_number3 and usr_number3 > usr_number2:
        print(f"""Mayor: {usr_number} 
Menor: {usr_number2}""")

    elif usr_number2 > usr_number3 and usr_number3 > usr_number:
        print(f"""Mayor: {usr_number2} 
Menor: {usr_number}""")

    else:
        print("Se ingresaron numeros iguales")


if __name__ == '__main__':
    define_mayor_menor()