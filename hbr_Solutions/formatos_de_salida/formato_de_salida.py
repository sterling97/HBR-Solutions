import time


usr_base = int(input("Digite la base: "))
usr_altura = int(input("Digite la altura: "))


area_triangulo = usr_base * usr_altura / 2


print(f'Area triangulo: {area_triangulo:,.2f}')
print(f'Area triangulo: $ {area_triangulo:,.2f}')
print(f'Area triangulo: {area_triangulo:,.2f}')
print(f'Area triangulo: {area_triangulo:,.0f}')


print(time.strftime("Hoy es %A, %d de %B del %Y %H:%M:%S"))
print(time.strftime("Hoy es %A %d/%m/%y"))
