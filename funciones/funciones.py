#crear contraseña aleatoria
def crear_contraseña(num):
    caracter = 'abcdefghijklm'
    num_entero = str(num)
    num = int(num_entero[0])
    print(num_entero)
    print(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num -5
    contraseña = f'{caracter[c1]}{caracter[c2]}{caracter[c3]}{num * 2}'
    print(contraseña)
crear_contraseña(9)