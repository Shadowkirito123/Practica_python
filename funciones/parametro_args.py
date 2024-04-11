#utilizando el parametro * como argumento (*args)
def suma(*numeros):
    return sum(numeros)
resultado = suma(5,9,4,3,8,10,50,5)
print(resultado)

#utilizando el parametro args 2
def suma(nombre,*numeros):
    return f'{nombre} la suma de tus numeros es {sum(numeros)}'
resultado = suma('Erick',5,9,4,3,8,10,50,5)
print(resultado)