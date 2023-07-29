# Listas son ordenadas, mutables y permiten duplicados
# animales = ['Perro', 'Gato', 'Pato', 'Escarabajo']
# animales.append('Raton')
# print(animales)

# animales = ['Perro', 'Gato', 'Pato', 'Escarabajo']
# animales_raros = animales.copy()
# print(animales_raros)
# print(len(animales_raros))

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# print(animales.count('Perro'))

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# print(animales.index('Escarabajo'))

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# animales.pop()
# print(animales)
# animales.pop(2)
# print(animales)

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# mas_animales=['Ballena', 'Lobo', 'Foca', 'Cangrejo']
# animales.extend(mas_animales)
# print(animales)
# animales.extend(['Hormiga', 'Mariposa'])
# print(animales)

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# mas_animales=['Ballena', 'Lobo', 'Foca', 'Cangrejo']
# animales += mas_animales
# print(animales)
# # print(animales + mas_animales)

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# animales.reverse()
# print(animales)

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# animales.remove('Gato')
# print(animales)

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# animales.clear()
# print(animales)

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# animales.sort(reverse=True)
# print(animales)

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
# animales.insert(3,'Armadillo')
# print(animales)

# animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo'] * 3
# print(animales)

animales = ['Perro', 'Perro', 'Gato', 'Pato', 'Pato', 'Escarabajo']
mas_animales = ['Ballena', 'Lobo', 'Foca', 'Cangrejo', animales]
otros_animales = ['Serpiente', mas_animales, 'Anaconda', 'Cocodrilo']

print(otros_animales)
print(otros_animales[0])
print(otros_animales[1][2])
print(otros_animales[1][4][2])
print('Escarabajo' in animales)
print(otros_animales[1:3])
print(otros_animales[:3])
print(otros_animales[2:])
print(otros_animales[1][4][1:4])
print(otros_animales[1][-1])
print(otros_animales)
otros_animales[1][0] = 'Pez'
print(otros_animales)
