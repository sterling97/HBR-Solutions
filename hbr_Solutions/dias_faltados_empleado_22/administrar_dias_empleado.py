# 22) Confeccionar una clase para administrar los días que han faltado los 3 empleados de una empresa.
# Definir un vector de 3 elementos de tipo string para cargar los nombres y una matriz irregular para
# cargar los días que han faltado cada empleado (cargar el número de día que faltó)
# Cada fila de la matriz representan los días de cada empleado.
# Mostrar los empleados con la cantidad de inasistencias.
# Cuál empleado faltó menos días.

employee = ['Jose', 'Carmen', 'Juana']
absence_from_work = ['3', '1', '2']


print(f'''Inasistencias de empleados: {employee[0]} ha faltado {absence_from_work[0]} veces.
Inasistencias de empleados: {employee[1]} ha faltado {absence_from_work[1]} veces.
Inasistencias de empleados: {employee[2]} ha faltado {absence_from_work[2]} veces.''' + '\n')

print(f'{employee[1]} fue quien falto menos con un total de {absence_from_work[1]} dias')