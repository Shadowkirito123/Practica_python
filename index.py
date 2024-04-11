# saludo = input('Hola como te llamas: ')
# print(f'saludos {saludo}')
# pregunta1 = input('¿Como te encuentras el dia de hoy?: ')
# signo_de_inte = pregunta1.startswith('¿')
# if signo_de_inte == True:
#     respuesta = input('Es eso una pregunta acaso?: ')
#     if respuesta == 'si':
#         print('Aqui no respondemos nada')
#     elif respuesta == 'no':
#         print('a pos bien')
# elif pregunta1 == 'Bien':
#     print('me alegro mucho')
# elif pregunta1 == 'Mal':
#     print('enserio cuanto lo siento')

# animales = input('Dime tres animales: ')
# separar_animales = animales.split(" " or ",")
# print(separar_animales)
# for separar in separar_animales:
#     if separar == 'gato':
#         continue
#     print(f'tienes un {separar}')

diccionario = {
    'nombre': 'erick',
    'apellido': 'rojas',
    'gato': 'juls'
}
print(diccionario['nombre'])
for datos in diccionario.items():
    Key = datos[0]
    Value = datos[1]
    print(f'la clave es {Key} y su valor es {Value}')