import tkinter as tk
def calcular_imc():
    root = tk.Tk()
    root.title('Calcule seu IMC')
    root.geometry('400x300')
    
    label = tk.Label(root, text='Calcule seu IMC', font=('Times New Roman', 24))
    label.pack(pady=20)

    frame_entrada = tk.Frame(root)
    frame_entrada.pack(pady=5)

    label_peso = tk.Label(frame_entrada, text='Peso (kg):', font=('Times New Roman', 16))
    label_peso.grid(row=0, column=0, padx=5, pady=5)

    peso_entry = tk.Entry(frame_entrada, font=('Times New Roman', 16))
    peso_entry.grid(row=0, column=1, padx=5, pady=5)

    label_altura = tk.Label(frame_entrada, text='Altura (m):', font=('Times New Roman', 16))
    label_altura.grid(row=1, column=0, padx=5, pady=5)

    altura_entry = tk.Entry(frame_entrada, font=('Times New Roman', 16))
    altura_entry.grid(row=1, column=1, padx=5, pady=5)

    def calcular():
        resultado = ''
        try:
            peso = float(peso_entry.get())
            altura = float(altura_entry.get())
            imc = peso / (altura ** 2)
            if imc < 18.5:
                resultado = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                resultado = 'Peso ideal'
            elif 25 <= imc < 29.9:
                resultado = 'Sobrepeso'
            elif 30 <= imc < 34.9:
                resultado = 'Obesidade'
            else:
                resultado = 'Obesidade extrema'
            label_resultado.config(text=f'IMC: {imc:.2f} - {resultado}')
        except ValueError:
            label_resultado.config(text='Por favor, insira valores válidos.')

    button_calcular = tk.Button(root, text="Calcular", font=('Times New Roman', 16), command=calcular)
    button_calcular.pack(pady=10)

    label_resultado = tk.Label(root, text='', font=('Times New Roman', 16))
    label_resultado.pack(pady=10)

    root.mainloop()
calcular_imc()