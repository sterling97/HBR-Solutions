# 21) Confeccionar una clase para administrar una matriz irregular de 5 filas y 1 columna la primer fila, 2
# columnas la segunda fila y así sucesivamente hasta 5 columnas la última fila (crearla sin la intervención
# del operador)
# Realizar la carga por teclado e imprimir posteriormente.

matrix = []

rows = int(input("Cantidad de Filas: "))
columns = int(input("Cantidad de columnas: "))


for i in range(rows):
    matrix.append([0]  * columns)
    matrix.append([1]  * columns)

for rows in range(rows):
    for columns in range(columns):
        matrix[rows] [columns] = int(input("Elemento %d, %d : " % (rows,columns)))

print(matrix)