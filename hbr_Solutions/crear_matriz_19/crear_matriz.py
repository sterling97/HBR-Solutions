# 19) Crear una matriz de 2 filas y 5 columnas. Realizar la carga de componentes por columna (es decir
# primero ingresar toda la primer columna, luego la segunda columna y así sucesivamente)


matrix = []

rows = int(input("Cantidad de Filas: "))
columns = int(input("Cantidad de columnas: "))


for i in range(rows):
    matrix.append([0]  * columns)

for rows in range(rows):
    for columns in range(columns):
        matrix[rows] [columns] = int(input("Elemento %d, %d : " % (rows,columns)))

print(matrix)