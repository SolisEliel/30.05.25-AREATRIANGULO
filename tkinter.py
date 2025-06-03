import tkinter as tk
from tkinter import messagebox

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


def calcular_area():
    try:
        base = float(entrada_base.get())
        altura = float(entrada2.get())
        triangulo = Triangulo(base, altura)
        area = triangulo.calcular_area()
        resultado_label.config(text=f"Área: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
        



ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("300x200")
ventana.config(bg="#AEBED9")


et1 = tk.Label(ventana, text="BASE:", bg="#AEBED9")
et1.pack(pady=5)

entrada_base = tk.Entry(ventana)
entrada_base.pack()

entrada_altura = tk.Label(ventana, text="ALTURA:", bg="#AEBED9")
entrada_altura.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Calcular área", command=calcular_area)
boton.pack(pady=10)

resultado_label = tk.Label(ventana, text="", font=("Arial", 12), bg="#AEBED9")
resultado_label.pack()


ventana.mainloop()
