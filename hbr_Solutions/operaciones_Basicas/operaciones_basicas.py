

number_1 = int(input('Ingrese el primer valor a procesar: '))
number_2 = int(input('Ingrese el segundo valor a procesar: '))

sum = number_1 + number_2
subtraction = number_1 - number_2
multiply = number_1 * number_2
division = number_1 / number_2
division_residue = number_1 % number_2


print(f"""
Primer valor {number_1}
Segundo valor {number_2}

La suma es: {sum}
La resta es: {number_1} - {number_2} = {subtraction}
La multiplicacion es: {multiply}
La division es: {division}
El residuo es: {division_residue}

""")