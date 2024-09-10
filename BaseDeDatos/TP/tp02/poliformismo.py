# Clase abstracta Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self, alimento):
        print(f"{self.nombre} está comiendo {alimento}")

    def sonido(self):
        pass  # Este método se implementará en las subclases


# Subclase Perro
class Perro(Animal):
    def sonido(self):
        print(f"{self.nombre} hace GUAU")


# Subclase Gato
class Gato(Animal):
    def sonido(self):
        print(f"{self.nombre} hace MIAU")


# Subclase Pájaro
class Pajaro(Animal):
    def sonido(self):
        print(f"{self.nombre} hace PIOPIO")


# Creamos objetos de diferentes clases
perro = Perro("BOBY")
gato = Gato("PINKY")
pajaro = Pajaro("PIOLIN")

# Llamamos a los métodos de cada objeto
perro.comer("HUESO")
perro.sonido()

gato.comer("PESCADO")
gato.sonido()

pajaro.comer("SEMILLAS")
pajaro.sonido()

# Utilizamos polimorfismo para llamar a los métodos comunes
animales = [perro, gato, pajaro]

for animal in animales:
    animal.comer("comida")
    animal.sonido()