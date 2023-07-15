# Operadores de Comparación | siempre devuelve un booleano true o false
cabello = "negro"
cabello_dos = "negro"
numero_decimal = 24.12
jordan = 23
messi = 10
mbappe = 10

comparacion_uno = cabello == numero_decimal
print(comparacion_uno)  # igual que

comparacion_dos = cabello == cabello_dos
print(comparacion_dos)

comparacion_tres = cabello != jordan
print(comparacion_tres)  # diferente que

comparacion_cuatro = cabello != cabello_dos
print(comparacion_cuatro)

comparacion_cinco = jordan > messi
print(comparacion_cinco)  # mayor que

comparacion_seis = jordan < messi
print(comparacion_seis)  # menor que

comparacion_siete = mbappe >= messi
print(comparacion_siete)  # mayor o igual que

comparacion_ocho = mbappe <= jordan
print(comparacion_ocho)  # menor o igual que
