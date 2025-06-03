class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

if __name__ == "__main__":
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))

        triangulo = Triangulo(base, altura)
        area = triangulo.calcular_area()

        print(f"El área del triángulo es: {area}")

    except ValueError:
        print("Error: solo se permiten valores numéricos.")
