# 20) Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las
# temperaturas medias mensuales de dichos paises.
# Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
# Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
# a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
# 185
# b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
# c - Calcular la temperatura media trimestral de cada país.
# e - Imprimr los nombres de las provincias y las temperaturas medias trimestrales.
# f - Imprimir el nombre de la provincia con la temperatura media trimestral mayor.


country = input('Ingrese el nombre del pais: ')
contry_upper = country.upper()


list_of_countries = ['CANADA', 'ALEMANIA', 'FRANCIA', 'ITALIA']
monthly_temperature = ['''La temperatura mensual de Canada: Enero: Minima = -11°C maxima = -3°C, 
                                Febrero: Minima = -11°C maxima = -2°C
                                Marzo: Minima = -6°C maxima = 3°C
                                Abril: Minima = 1°C maxima = 11°C
                                Mayo: Minima = 6°C maxima = 18°C
                                Junio: Minima = 11°C maxima = 23°C
                                Julio: Minima = 14°C maxima = 27°C
                                Agosto: Minima = 13°C maxima = 25°C
                                Septiempre: Minima = 9°C maxima = 21°C
                                Octubre: Minima = 3°C maxima = 14°C
                                Noviembre: Minima = -1°C maxima = 7°C
                                Diciembre: Minima = -8°C maxima = 0°C''', 
                        """La temperatura mensual de Alemania: Enero: Minima = -3°C maxima = 2°C,
                                Febrero: Minima = -2°C maxima = 2°C
                                Marzo: Minima = 0°C maxima = 8°C
                                Abril: Minima = 4°C maxima = 13°C
                                Mayo: Minima = 8°C maxima = 18°C
                                Junio: Minima = 11°C maxima = 22°C
                                Julio: Minima = 13°C maxima = 23°C
                                Agosto: Minima = 12°C maxima = 23°C
                                Septiempre: Minima = 9°C maxima = 18°C
                                Octubre: Minima = 6°C maxima = 13°C
                                Noviembre: Minima = 2°C maxima = 7°C
                                Diciembre: Minima = -1°C maxima = 3°C""",
                        """La temperatura mensual de Francia: Enero: Minima = 1°C maxima = 6°C,
                                Febrero: Minima = 1°C maxima = 7°C
                                Marzo: Minima = 3°C maxima = 11°C
                                Abril: Minima = 6°C maxima = 14°C
                                Mayo: Minima = 9°C maxima = 18°C
                                Junio: Minima = 12°C maxima = 21°C
                                Julio: Minima = 14°C maxima = 21°C
                                Agosto: Minima = 14°C maxima = 24°C
                                Septiempre: Minima = 11°C maxima = 24°C
                                Octubre: Minima = 8°C maxima = 15°C
                                Noviembre: Minima = 4°C maxima = 9°C
                                Diciembre: Minima = 2°C maxima = 7°C,""",
                        """La temperatura mensual de Italia: Enero: Minima = 2°C maxima = 12°C,
                                Febrero: Minima = 3°C maxima = 13°C
                                Marzo: Minima = 4°C maxima = 16°C
                                Abril: Minima = 7°C maxima = 19°C
                                Mayo: Minima = 11°C maxima = 23°C
                                Junio: Minima = 14°C maxima = 27°C
                                Julio: Minima = 17°C maxima = 31°C
                                Agosto: Minima = 17°C maxima = 31°C
                                Septiempre: Minima = 14°C maxima = 27°C
                                Octubre: Minima = 10°C maxima = 22°C
                                Noviembre: Minima = 6°C maxima = 17°C
                                Diciembre: Minima = 3°C maxima = 13°C,
                                """]


quarterly_temperature = ["""Temperatura media del primer trimestre: -8°C
                            Temperatura media del segundo trimestre: 23°C
                            Temperatura media del segundo trimestre: 36°C
                            Temperatura media del segundo trimestre: 15°C""",
                        """Temperatura media del primer trimestre: 7°C
                            Temperatura media del segundo trimestre: 25°C
                            Temperatura media del segundo trimestre: 32°C
                            Temperatura media del segundo trimestre: 19°C""",
                        """Temperatura media del primer trimestre: 9°C
                            Temperatura media del segundo trimestre: 26°C
                            Temperatura media del segundo trimestre: 37°C
                            Temperatura media del segundo trimestre: 15°C""",
                        """Temperatura media del primer trimestre: 16°C
                            Temperatura media del segundo trimestre: 33°C
                            Temperatura media del segundo trimestre: 46°C
                            Temperatura media del segundo trimestre: 23°C"""]


def show_data():
    if contry_upper == list_of_countries[0]:
        print(monthly_temperature[0])
        print(quarterly_temperature[0])
    elif contry_upper == list_of_countries[1]:
        print(monthly_temperature[1])
        print(quarterly_temperature[1])
    elif contry_upper == list_of_countries[2]:
        print(monthly_temperature[2])
        print(quarterly_temperature[2])
    elif contry_upper == list_of_countries[3]:
        print(monthly_temperature[3])
        print(quarterly_temperature[3])
    else:
        print('Ingreso de forma incorrecta el nombre del pais.')


print('La temperatura media trimestral mas alta es: Italia' + '\n')


if __name__ == '__main__':
    show_data()
