# 5) Crear un programa que pida una letra al usuario y diga si se trata de una vocal.

usr_lyrics = input('Introduzca una letra: ')


vowels = ['a', 'e', 'i', 'o', 'u']


if usr_lyrics in vowels:
    print('La letra suministrada es una vocal')
else:
    print('No es una vocal')