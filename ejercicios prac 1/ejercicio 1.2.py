frase = input('Decime una frase y te calculo la cantidad de tiempo que tardarias en decirla: ')
palabras_contadas = frase.split(' ')
cantidad_de_palabras = len(palabras_contadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlas')
print(f'dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos en decirla')
if cantidad_de_palabras > 120:
    print('Para flaco tampoco me cuentes tu vida')