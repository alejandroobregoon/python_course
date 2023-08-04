for num in range(2, 10, 2):
    print("El numero es {0}".format(num))
    # print(f"El numero es {num}")

print('\n')

for i in range(1, 14):
    print("La multiplicación de {0} x {1} = {2}".format(i - 1, 8, (i * 8) - 8))
    # print(f"La multiplicación de {i} x {8} = {i * 8}")
    # print("La multiplicación de {0} x {1} = {2}".format(i, 8, i * 8))

print('\n')

recTupla = ('Martina', 'Alicia', 1223, 123.234, True, False, 'Maria')
recTupla2 = ('Martina', 'Alicia', 'Maria', 'Sofia')
# print('Martina' in recTupla)

for values in range(len(recTupla)):
    print(recTupla[values])

print('\n')

for values in recTupla2:
    print('La cantidad de caracteres de {0} es {1}: '.format(values, len(values)))

print('\n')

recoLista = ['Goku', 'Vegeta', 'Broly', 'Cell']

for dbz in recoLista:
    print(dbz)

print('\n')

for i in range(len(recoLista)):
    print(recoLista[i])

print('\n')

recoSet = {1, 2, 3, 4, 5}
recoSet2 = {'Oso', 'Serpiente', 'Delfin'}
print('Oso' in recoSet2)
print(6 not in recoSet)

for animales in recoSet2:
    print(animales)

print('\n')

recoDicti = {'España': 'Madrid', 'Peru': 'Lima', 'Inglaterra': 'Londres'}
print(recoDicti.get('España', 'No se encontro'))
print(recoDicti['Peru'])
for indice, paises in enumerate(recoDicti, start=0):
    print("El indice es {0} según el país {1} y tiene {2} letras".format(indice, paises, len(paises)))
