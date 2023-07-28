# len()
# cadena="Esto es una cadena"
# print(len(cadena))

# .upper()
# cadena_upper = "esto es una palabra en minuscula convertida a mayusucla"
# print(cadena_upper.upper())

# .lower()
# cadena_lower = "ESTO ES UNA CADENA EN MAYUSCULAS"
# print(cadena_lower.lower())

# .capitalize()
# cadena_cplz = "hola soy una cadena"
# print(cadena_cplz.capitalize())

# .find()
# cadena_fnd = "Esto es una cadena cadena cadena"
# print(cadena_fnd.find('u'))
# print(cadena_fnd.find('es'))
# print(cadena_fnd.rfind('cadena',0, 26))
# print(cadena_fnd.rfind('marvel'))

# .index()
# cadena_idx = "Esto es una cadena cadena cadena"
# print(cadena_idx.index('a'))
# print(cadena_idx.index('ena'))
# print(cadena_idx.rindex('cad', 0, 26))
# print(cadena_idx.rindex('dc'))

# .strip()
# cadena_stp = "  -- Esto es una cadena muy larga --  "
# print(cadena_stp.strip().strip('-').strip())
# print(cadena_stp.rstrip(' -'))
# print(cadena_stp.lstrip().lstrip('-'))

# .split()
# cadena_splt = "Esto es una cadena de tipo slipt"
# cadena_splt_2 = "Esto|es|una cadena|de tipo slipt"
# cadena_spltlns="Esto\nes\nuna\ncadena"
# print(cadena_splt.split())
# print(cadena_splt_2.split('|'))
# print(cadena_splt_2.split('|', 1))
# print(cadena_splt.rsplit(' ', 2))
# print(cadena_spltlns.splitlines())

# ''.join()
# animales = ['Gato', 'Perro', 'Dino', 'Armadillo', 'Rino']
# print(' '.join(animales))
# print(','.join(animales))
# print('-'.join(reversed(animales)))

# .replace()
# cadena_rplc = "Esto es una cadena a reemplazar reemplazar, reemplazar"
# print(cadena_rplc.replace('reemplazar', 'cambiar'))
# print(cadena_rplc.replace('reemplazar', 'cambiar', 1))
## otro metodo a cambiar #30 - #42
# new_cadena = cadena_rplc[:32] + "cambiar al metodo antiguo" + cadena_rplc[42:]
# print(new_cadena)

# .count()
# cadena_cnt="Esto es un hola mundo por el mundo para el mundo"
# print(cadena_cnt.count('mundo'))
# print(cadena_cnt.count('mundo',20))

# .zfill()
# cadena_zfll= "12345"
# print(cadena_zfll.zfill(7))

# .center() , .ljust(), .rjust()
# cadena_cnt = "¡Hola Mundo!"
# cadena_ljt = "12345"
# cadena_rjt = "1234"
#
# print(cadena_cnt.center(30, ' '))
# print(cadena_cnt.center(30, '*'))
# print(cadena_ljt.ljust(8, '%'))
# print(cadena_rjt.rjust(8, '0'))

# .format() , .format_map()
# nombre = "Juan"
# edad = 23
# sueldo = 2300.5648
#
# print("Mi nombre es {}, tengo la edad de {} y el sueldo es {}".format(nombre, edad, sueldo))
# print("Mi nombre es {nmb}, tengo la edad de {ed} y el sueldo es {sld:.2f}".format(nmb=nombre, ed=edad, sld=sueldo))
# print("Mi nombre es {1}, tengo la edad de {0} y el sueldo es {2:.2f}".format(nombre, edad, sueldo))
#
# datos_personas = {
#     'nombre': 'Juan',
#     'edad': 23,
#     'sueldo': 2300.5648
# }
# print("Mi nombre es {nombre}, tengo la edad de {edad} y el sueldo es {sueldo:.2f}".format_map(datos_personas))
# print("La numero es {edad:05d}".format_map(datos_personas))

# .swapcase()
# cadena_swpcs = "Esto ES una CadeNa"
# cadena_swpcs2 = "esto es una cadena"
# cadena_swpcs3 = "ESTO ES UNA CADENA"
# print(cadena_swpcs.swapcase())
# print(cadena_swpcs2.swapcase())
# print(cadena_swpcs3.swapcase())

# .title()
# cadena_ttl = "esto es una cadena"
# print(cadena_ttl.title())

# .startWith()
# cadenastrwth = "Hola brother"
# print(cadenastrwth.startswith('H'))
# print(cadenastrwth.lower().startswith('h'))
# print(cadenastrwth.startswith('b', 5, 9))

# .endWith()
# cadenaendwth = "hola brother"
# print(cadenaendwth.endswith('r'))
# print(cadenaendwth.upper().endswith('R'))
# print(cadenaendwth.endswith('o', 0, 8))

# .isspace()
# cadenaspc = "       \t\t       "
# print(cadenaspc.isspace())

# .isdigit() 0-9
# cadenadg = "0123456789"
# cadenadg2 = " 0123456789"
# print(cadenadg.isdigit())
# print(cadenadg2.isdigit())

# .isaplha()
# cadenaalp = "abcxyz"
# cadenaalp2 = " !abcxy-cc1 "
# print(cadenaalp.isalpha())
# print(cadenaalp2.isalpha())

# .isalnum()
cadenaalpnm = "hola123"
cadenaalpnm2 = "hola 123"
print(cadenaalpnm.isalnum())
print(cadenaalpnm2.isalnum())
