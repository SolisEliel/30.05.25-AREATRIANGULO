class Triangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def resultado(self):
        return (self.base * self.altura) / 2

if __name__ == "__main__":

    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    triangulo = Triangulo(base, altura)

    r = triangulo.resultado()

    print(f"El área del triángulo es: {r}")
