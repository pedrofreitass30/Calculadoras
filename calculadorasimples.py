import tkinter as tk
def calcular():
    root = tk.Tk()
    root.title("Calculadora Simples")
    root.geometry("300x400")

    label = tk.Label(root, text="Calculadora Simples", font=("Times New Roman", 24))
    label.pack(pady=20)

    a = tk.Entry(root, font=("Arial", 16))
    a.pack(pady=5)

    b = tk.Entry(root, font=("Arial", 16))
    b.pack(pady=5)

    def somar():
        try:
            valor_a = int(a.get())
            valor_b = int(b.get())
            resultado = valor_a + valor_b
            label_resultado.config(text=f"Resultado soma: {resultado}")
        except ValueError:
            label_resultado.config(text="Por favor, insira números válidos.")
    def subtrair():
        try:
            valor_a = int(a.get())
            valor_b = int(b.get())
            resultado = valor_a - valor_b
            label_resultado.config(text=f"Resultado subtração: {resultado}")
        except ValueError:
            label_resultado.config(text="Por favor, insira números válidos.")
    def multiplicar():
        try:
            valor_a = int(a.get())
            valor_b = int(b.get())
            resultado = valor_a * valor_b
            label_resultado.config(text=f"Resultado multiplicação: {resultado}")
        except ValueError:
            label_resultado.config(text="Por favor, insira números válidos.")
    def dividir():
        try:
            valor_a = int(a.get())
            valor_b = int(b.get())
            if valor_b == 0:
                label_resultado.config(text="Divisão por zero não é permitida.")
                return
            resultado = valor_a / valor_b
            label_resultado.config(text=f"Resultado divisão: {resultado}")
        except ValueError:
            label_resultado.config(text="Por favor, insira números válidos.")

    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=5)

    button_somar = tk.Button(frame_botoes, text="+", font=("Times New Roman", 16), command=somar)
    button_somar.pack(side=tk.LEFT, padx=5)


    button_subtrair = tk.Button(frame_botoes, text="-", font=("Times New Roman", 16), command=subtrair)
    button_subtrair.pack(side=tk.LEFT, padx=5)

    button_multiplicar = tk.Button(frame_botoes, text="*", font=("Times New Roman", 16), command=multiplicar)
    button_multiplicar.pack(side=tk.LEFT, pady=5)

    button_dividir = tk.Button(frame_botoes, text="/", font=("Times New Roman", 16), command=dividir)
    button_dividir.pack(side=tk.LEFT, pady=5)

    label_resultado = tk.Label(root, text="Resultado", font=("Times New Roman", 16))
    label_resultado.pack(pady=10)


    root.mainloop()
calcular()