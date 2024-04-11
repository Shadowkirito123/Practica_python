animales =['perro', 'gato', 'loro']
numero = [10, 25, 30]

#Recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#recorreindo la lista de numero y multiplicando
for numeros in numero:
    resultado = numeros * 10
    print(resultado)

#recorriendo dos listas al mismo tiempo
for animal, numeros in zip(animales, numero):
    print(f'El animal es: {animal}')
    print(f'El numero es: {numeros}')