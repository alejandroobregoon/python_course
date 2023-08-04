"""Contador ascendente: Escribe un programa que cuente del 1 al 10 y muestre los números en cada iteración.
"""
import random

# contador = 1
#
# while contador <= 10:
#     print("El número es: {0}".format(contador))
#     contador += 1


"""Contador descendente: Escribe un programa que cuente desde 10 hasta 1 y muestre los números en cada iteración.
"""

# contador = 10
#
# while contador >= 1:
#     print("El número es: {}".format(contador))
#     contador -= 1

"""Suma de números: Pide al usuario que ingrese un número positivo. Luego, utiliza un bucle while para calcular la suma de todos los números desde 1 hasta el número ingresado.
"""

# numero = int(input("Ingresa un numero: "))
# suma = 0
# if numero > 0:
#     for i in range(1, numero + 1):
#         suma = suma + i
#     print("La sumatoria de todos los números positivos es de: {}".format(suma))
# else:
#     print("Ingrese un número positivo válido")

"""Adivinar el número: Escribe un programa que genere un número aleatorio entre 1 y 100. Luego, pide al usuario que adivine el número. Si el usuario adivina el número correcto, muestra un mensaje de felicitaciones. Si el número es mayor o menor al número objetivo, muestra una pista y permite al usuario intentarlo nuevamente. """

# while True:
#     numero = int(input("Ingrese un numero: "))
#
#     for i in range(1):
#         rango = random.randrange(1, 100, 1)
#         # print(rango)
#
#     if numero == rango:
#         print(
#             " Felicitaciones has conseguido adivinar el numero aleatorio fue {0} y tu numero es {1}".format(rango, numero))
#         break
#     else:
#         if numero > rango or numero < rango:
#             print("MMM.. no lo conseguistes vuelve a intentarlo el numero aletorio fue {0} y tu numero es {1}".format(
#                 rango, numero))

"""Tabla de multiplicar: Pide al usuario que ingrese un número entero. Luego, muestra la tabla de multiplicar de ese número del 1 al 10."""

# numero = int(input("Ingrese un numero: "))
#
# for i in range(1, 11):
#     print("La multiplicación de {0} x {1} = {2}".format(i, numero, i * numero))

"""Calculadora simple: Crea una calculadora simple que permita al usuario ingresar dos números y una operación (suma, resta, multiplicación o división). Utiliza un bucle while para permitir que el usuario realice varias operaciones antes de salir del programa."""

# class Calculator:
#     def __init__(self, num1=0, num2=0):
#         self.num1 = num1
#         self.num2 = num2
#
#     def inicializador(self):
#         while True:
#             print("WELCOME TO CALCULATOR")
#             print("1.- SUMA")
#             print("2.- RESTA")
#             print("3.- MULTIPLICACIÓN")
#             print("4.- DIVISIÓN")
#             print("0.- SALIR")
#             print("************************")
#             op = int(input("Ingrese una opción válida: "))
#             print("************************")
#             if op > 0 and op < 5:
#                 self.num1 = int(input("Ingrese el primer digito: "))
#                 self.num2 = int(input("Ingrese el segundo digito: "))
#             print("************************\n")
#
#             if op == 1:
#                 print("La suma de {0} y {1} es: {2}\n".format(self.num1, self.num2, (self.num1 + self.num2)))
#             elif op == 2:
#                 print("La resta de {0} y {1} es: {2}\n".format(self.num1, self.num2, (self.num1 - self.num2)))
#             elif op == 3:
#                 print("La multiplicación de {0} y {1} es: {2}\n".format(self.num1, self.num2, (self.num1 * self.num2)))
#             elif op == 4:
#                 print("La división de {0} y {1} es: {2:.2f}\n".format(self.num1, self.num2, (self.num1 / self.num2)))
#             else:
#                 break
#
#             if not self.preguntarNuevo():
#                 break
#
#     def preguntarNuevo(self):
#         ques = str(input("¿Quieres realizar otra operación S/N?: "))
#         continuar = True
#         if ques.isalpha():
#             if ques.upper() == "S":
#                 print("Ok! Continua\n")
#             elif ques.upper() == "N":
#                 print("Good Bye!\n")
#                 continuar == False
#         return continuar
#
#
# cal = Calculator()
# cal.inicializador()

"""Contador de dígitos: Pide al usuario que ingrese un número entero. Luego, cuenta y muestra cuántos dígitos tiene el número."""

# while True:
#     numero = int(input("Ingrese un numero: "))
#     numero2 = len(str(numero))
#     int(numero2)
#     print(numero2)
#
#     while True:
#         ques = str(input("Quires seguir preguntando la cantidad de digitos S/N: "))
#         con = True
#         if ques.upper() == "S":
#             print("¡Continua!\n")
#             break
#         elif ques.upper() == "N":
#             print("Good Byee!\n")
#             con = False
#             break
#         else:
#             print("!!!!! ADVERTENCIA!!!!! #Ingresa solo S/N\n")
#             pass
#
#     if not con:
#         break

"""Patrón triangular: Escribe un programa que imprima un patrón triangular con asteriscos. El usuario debe ingresar el número de filas del patrón."""

"""filas = int(input("Ingrese el numero de filas: "))
for i in range(filas):
    vari = "*".ljust(filas, "*")
    print(vari)
    filas -= 1
    for k in range(filas):
        print("", end="")
        """

"""
asterico = "*"
fila = 10
columnas = 20

for i in range(fila):
    print("")
    for k in range(columnas):
        print(asterico, end="")
"""

filas = int(input("Ingrese el numero de filas: "))

for i in range(filas):
    vari = " " * (filas - i - 1) + "* " * (i + 1)
    print(vari)
