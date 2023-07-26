def blanco():
    pass


class Persona:
    # Pongo por defecto valores para ya no ponerlo en el objeto creado cuando instancio la clase Persona
    def __init__(self, nombre="", apellido="", talla=0, sueldo=0):
        self.nombre = nombre
        self.apellido = apellido
        self.talla = talla
        self.sueldo = sueldo

    def saludar(self):
        self.nombre = input("Ingrese un nombre para saludar: ")
        print(f"Hola {self.nombre} \n")

    def datos_personales(self):
        self.nombre
        self.apellido = input("Ingrese su apellido: ")
        print(f"Bienvenido {self.nombre} {self.apellido} a tu primera clase \n")

    def datos_secundarios(self):
        self.talla = float(input("Ingrese su talla: "))
        print(f"Su talla es de {self.talla} cm \n")

    def ingresos(self):
        self.sueldo = float(input("Ingrese su sueldo: "))
        print(f"Sueldo o ingresos es de {self.sueldo} \n")


persona1 = Persona()
persona1.saludar()
persona1.datos_personales()
persona1.datos_secundarios()
persona1.ingresos()
