# #crear contraseña aleatoria usando print
# def crear_contraseña(num):
#     caracter = 'abcdefghijklm'
#     num_entero = str(num)
#     num = int(num_entero[0])
#     print(num_entero)
#     print(num_entero[0])
#     c1 = num - 2
#     c2 = num
#     c3 = num -5
#     contraseña = f'{caracter[c1]}{caracter[c2]}{caracter[c3]}{num * 2}'
#     print(contraseña)
# crear_contraseña(9)

#crear contraseña aleatoria usando return
def crear_contraseña(num):
    caracter = 'abcdefghijklm'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num -5
    contraseña = f'{caracter[c1]}{caracter[c2]}{caracter[c3]}{num * 2}'
    return contraseña,num

#desempaquetando la funcion con return
password, primer_numero = crear_contraseña(9)

#mostrar el resultado
print(f'su contrasena es: {password}')
print(f'y el numero usado para crearla fue el: {primer_numero}')