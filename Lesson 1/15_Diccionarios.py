# dictPaises = {'Espania': 'Madrid', 'Peru': "Lima", 'Alemania': 'Berlin', 'Rusia': 'Moscow'}
# dictMasPaises = {'Salvador': 'San Salvador', 'Ukrania': 'Kiev', 'Mexico': 'Ciudad de Mexico'}
#
# dictPaises.update(dictMasPaises)
# print(dictPaises)
#
# del dictPaises['Mexico']
# print(dictPaises)
#
# dictOtrosPaises = {'Brasil': 'Brasilia', 'Uruguay': 'Montevideo', 'Alemania': 'Hamburgo'}
# dictPaises.update(dictOtrosPaises)
# print(dictPaises)
# dictPaises['Alemania'] = 'Berlin'
# print(dictPaises)

# dictPaises.pop('Espania')
# print(dictPaises)

# dictPaises.clear()
# print(dictPaises)

# dictPaises_nuevo = dictPaises.copy()
# print(dictPaises_nuevo)

# print(dictPaises.get('Espania','No se encontro'))
# print(dictPaises.get('Espanisa'))

# print(dictPaises.keys())
# print(dictPaises.values())
# print(dictPaises.items())

# print(dictPaises.setdefault('Espansia', 'No se encontro'))
# print(dictPaises)

# print(dictPaises.popitem())
# print(dictPaises.popitem())
# print(dictPaises.popitem())
# print(dictPaises.popitem())
# print(dictPaises.popitem())

# lista = ['Gallo', 'Caballo', 'Gato']
# tupla = ('Gallina', 'Yegua', 'Gata')
#
# dictNuevo = {}
#
# dictNuevo = dictNuevo.fromkeys(lista, "No definido")
# # print(dictNuevo)
#
# for index, key in enumerate(dictNuevo):
#     if index < len(dictNuevo):
#         dictNuevo[key] = tupla[index]
# print(dictNuevo)
#


#
# for indce, clave in enumerate(dictNuevo):
#     if indce < len(dictNuevo):
#         dictNuevo[clave] = tupla[indce]
# print(dictNuevo)
#
# dictNuevo = dict(zip(lista, tupla))
# print(dictNuevo)
#
#
# for i in range(len(lista)):
#     dictNuevo[lista[i]] = tupla[i]
# print(dictNuevo)
#
#
# for i in range(len(lista)):  # 2
#     nuevaCadena = lista[i] + ' ' + tupla[i]
#     modNuevaCadena = nuevaCadena.split()
#     dictNuevo[modNuevaCadena[0]] = modNuevaCadena[1]
# print(dictNuevo)
