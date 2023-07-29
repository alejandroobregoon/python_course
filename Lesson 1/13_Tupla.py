# son ordenadas, no se pueden inmutar y si aceptan duplicado
# animales = ('Gallo', 'Perro', 'Gato', 'Gato', 'Pollo', 'Escarabajo', 123, 1.25, True)
# print(type(animales))
# print(animales.count('Gato'))

animales = 'Gallo', 'Perro', 'Gato', 'Gato', 'Pollo', 'Escarabajo', 123, 1.25, True
milista = list(animales)
print(milista)

peces = ['Papayaso', 'Caballa', 'Espada', 'Espada', 'Caballa']
peces_ = tuple(peces)
print(peces_)

print(peces_.count('Espada'))
print(peces_.count('Caballa'))
print(len(peces_))
lista = ' '.join(reversed(peces_))
print(lista)
nueva = lista.split(' ')
tupla = tuple(nueva)
print(tupla)
print(type(tupla))

print(tupla.index('Caballa',2))
