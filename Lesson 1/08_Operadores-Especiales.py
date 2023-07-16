# Operadores Especiales siempre devuelven un booleano
# IS | sirve para ver si dos objetos son el mismo objeto en la memoria | comparan la identidad del obj
a = [1, 2, 3]
b = a
c = [123, 213]  # *
print(b is a)
print(c is a)  # *

# IS NOT | sirve para ver si dos objetos no son el mismo objeto en la memoria | compara la iden. del obj
x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)
print(x is y)
print(x == y)  # es para comparar los valores los otros no

# IN | sirve para ver si un elemento se encuentra en una secuencia
z= [1,2,3,4,5,6,7,8,9]
print(5 in z)
print(57 in z)

# NOT IN |  sirve para ver si un elemento no se encuentra en una secuencia
h= [100,101,102,103,104]
print(106 not in h)
print(103 not in h)