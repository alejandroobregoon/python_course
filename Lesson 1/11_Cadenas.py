cadena = "hello,word"
cadena2 = "Manela es una chica linda"
print(len(cadena))
print(cadena.upper())
print(cadena.lower())
print(cadena.split(','))
print(cadena.upper().startswith('H'))
print(cadena.endswith('d'))
print(cadena.isupper())
print(cadena.islower())
print(''.join(reversed(cadena)))

for i in range(len(cadena)):
    print(cadena[len(cadena) - i - 1])

string = "Diploma en el 2023"
print(string[:7] + " conseguida" + string[-11:])


saludo = "Hola"

print(saludo.upper().endswith("A"))
print(saludo.lower().startswith("h"))

frase = "Quiero comer un pastel de chocolate"
print(frase.split())

c = frase[:6] + " tragar" + frase[-23:]
print(c)


