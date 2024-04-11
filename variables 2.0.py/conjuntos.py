# conjunto = set(['dato1'])
# print(type(conjunto))

# conjunto = frozenset({'hola'})
# conjunto2 = {conjunto, 'despedido'}
# print(conjunto2)

conjunto1 = {1,2,4,5,6}
conjunto2 = {8,9,7}
# resultado = conjunto2.issuperset(conjunto1)
# resultado2 = conjunto2 > conjunto1
resultado2 = conjunto2.isdisjoint(conjunto1)
print(resultado2)