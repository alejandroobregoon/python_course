# *** Persona and Bank ***
# class Persona:
#     def __init__(self, nombre="", apellido="", edad=0, talla=0.0, sueldo=0.0):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.talla = talla
#         self.sueldo = sueldo
#
#     def saludar(self):
#         self.nombre = input("¿Cuál es tu nombre?: ")
#         print(f"Hola {self.nombre}\n")
#
#     def datos_personales(self):
#         self.nombre
#         self.apellido = input(f"¿Cuál tu apellido {self.nombre}?: ")
#         self.edad = int(input(f"¿Cuál es tu edad, Mr.{self.nombre} {self.apellido}?: "))
#         self.talla = float(input(f"¿Cuánto mides Mr.{self.nombre} {self.apellido}?: "))
#         self.sueldo = float(input(f"¿Cuánto es su salario total Mr.{self.nombre} {self.apellido}?: "))
#         print(
#             f"\nHola Mr.{self.nombre} {self.apellido}, tiene {self.edad} años, mides {self.talla} cm, tu salario bruto es de S/." + "{sld:.2f} nuevos soles".format(
#                 sld=self.sueldo))
#
#
# persona1 = Persona()
# persona1.saludar()
# persona1.datos_personales()


class Bank:
    def __init__(self, usuario="", cuentas="", saldo=0.0, retiro=0.0, deposito=0.0):
        self.usuario = usuario
        self.cuentas = cuentas
        self.saldo = saldo
        self.retiro = retiro
        self.deposito = deposito
        self.cuentas = {
            '123456789': {
                'nombre': 'Alejandro',
                'monto': 3000
            },
            '356457896': {
                'nombre': 'Javier',
                'monto': 3652
            }
        }

    def iniciar_operaciones(self):
        cuenta = str(input('Ingrese su numero de cuenta: '))
        if cuenta.isdigit():
            if cuenta in self.cuentas:
                usuario = self.cuentas[cuenta]['nombre']
                saldo = self.cuentas[cuenta]['monto']

                while True:
                    print(f"Bienvenido {usuario}\n")
                    print("OPERACIONES")
                    print("1.- Consultar saldo")
                    print("2.- Depositar")
                    print("3.- Retirar")
                    print("4.- Salir\n")

                    opcion = int(input("Ingrese su opcion del 1 al 4: \n"))

                    if opcion in range(1, 5):
                        if opcion == 1:
                            print(f"Estimado {usuario} su saldo es de S/.{saldo} nuevos soles")

                        elif opcion == 2:
                            monto = int(input("Monto a depositar: "))
                            saldo += monto
                            print(f"Su nuevo saldo es S/.{saldo} nuevos soles")

                        elif opcion == 3:
                            monto_resta = int(input("Saldo a retirar: "))
                            saldo -= monto_resta
                            print(f"Su nuevo saldo es de S/.{saldo} nuevos soles")

                        elif opcion == 4:
                            break

                        if not self.pregunta_nuevo():  # True o False
                            break
                    else:
                        print("\nIngrese un valor valido del 1 - 4\n\n")

            else:
                print("Esta cuenta no existe en la BD")

        else:
            print("Solo ingrese caracteres numericos del 1 al 4! GRACIAS!!")

    def pregunta_nuevo(self):
        continuar = True
        op = str(input("Quieres hacer otra operacion S/N: "))
        if op.isalpha():
            if op.upper() == 'S':
                print("Ok!")
            elif op.upper() == 'N':
                print("Bye!")
                continuar = False
        return continuar


bank1 = Bank()
bank1.iniciar_operaciones()
