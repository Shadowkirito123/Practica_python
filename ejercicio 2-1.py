#Falto el profe y su asistete asi que los laumnos se las arrglaron para definir un prfesor y un asistente colocando el mayor como profesor y el menor como asistente
#Primero creamos una funcion para definir el profe y su asistente por su edad
def obtener_compañeros_de_lsita(cantida_de_compañeros):
    compañeros = []
    #definimos un for que recorra la cantidad de compañeros para preguntarles y usamos range para recorrer segun la cantidad de compañeros
    for i in range(cantida_de_compañeros):
        nombre = input('¿cual es tu nombre?: ')
        edad = int(input('¿cual es tu edad?: '))
        #agregamos el nombre y la edad en una variable que va a contener una tupla que tendra el nombre y la edad
        compañero = (nombre, edad)
        compañeros.append(compañero)
    #lo ordenamos de menor a mayor con el metodo de sort() usando lambda hacemos que tome lo ordene por el valor de la key indicando la posicion con [1] 
    compañeros.sort(key = lambda x:x[1])
    #aqui decimos que del primer elemento tome el primer valor osea el nombre
    asistente = compañeros[0][0]
    #aqui decimos que del ultimo elemento tome el primer valor osea el nombre
    profesor = compañeros[-1][0]
    return asistente,profesor
#desempaquetamos
asistente,profesor= obtener_compañeros_de_lsita(3)
print(f'El profesor es {profesor} y su asistente es {asistente}')