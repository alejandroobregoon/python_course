# # No son ordenados, son mutables y no aceptan duplicados, no se puede acceder a elementos con indice
# """
# numeros = {
#     5, 4, 2, 1, 3, 6, 7, 9, 8
# }
#
# print(type(numeros))
# print(numeros)
#
# numeros.pop()
# print(numeros)
# numeros.pop()
# print(numeros)
#
# numeros.remove(5)
# print(numeros)
#
# numeros.add(5)
# print(numeros)
#
# numeros.discard(5)
# print(numeros)
#
# nuevo = numeros.copy()
# print(nuevo)
#
# nuevos2 = {3, 4, 5, 6, 7, 8, 9}
#
# nuevo.update(nuevos2)
# print(nuevo)
# print(nuevo)
# texto = {56, 58, 57, 59, 61, 60}
# text2 = {66, 68, 67, 69, 71, 70}
# print(4 in nuevo)
# print(nuevo.union(texto))
# print(nuevo | texto | text2)
# print(nuevo.union(texto).union(text2))
# """

# No son ordenados, son mutables y no aceptan duplicados
# Tambien pueden ser inmutables con frozenset()

# fruta3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(fruta1)
# fruta1.add('Kiwi')
# print(fruta1)
# nueva_fruta1 = fruta1.copy()
# print(nueva_fruta1)
# nueva_fruta1.discard('Perita')
# print(nueva_fruta1)
# nueva_fruta1.add('Perita')
# print(nueva_fruta1)
# nueva_fruta1.discard('Perita')
# # print(nueva_fruta1)
# # nueva_fruta1.remove('Perita')
# print(nueva_fruta1)
# nueva_fruta1.pop()
# print(nueva_fruta1)
# nueva_fruta1.pop()
# print(nueva_fruta1)
# nueva_fruta1=list(nueva_fruta1)
# nueva_fruta1.reverse()
# print(nueva_fruta1)
# nueva_fruta1=set(nueva_fruta1)
# print(nueva_fruta1)
#
# nueva_fruta1.update(('Mango', 'Naranja','Kiwi', 'Melon'))
# print(nueva_fruta1)


fruta1 = {'Manzana', 'Uva', 'Pera', 'Granadilla', 'Naranja'}
fruta2 = {'Manzana', 'Granadilla'}
fruta3 = {'Durazno', 'Granada', 'Kiwi', 'Guanabana', 'Sandia'}
# print(fruta1.union(fruta2))
# print(fruta1 | fruta2)
# print(fruta1.intersection(fruta2))
# print(fruta1 & fruta2)
# print(fruta1.difference(fruta2))
# print(fruta1 - fruta2)
# print(fruta2.difference(fruta1))
# print(fruta2 - fruta1)

print(fruta1.symmetric_difference(fruta2))
print(fruta2.issubset(fruta1))

# setsolo=set()
# print(type(setsolo))
# print(setsolo)