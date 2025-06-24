import tkinter as tk
def tela():
    # Criando a janela principal
    root = tk.Tk()
    root.title("Soma")
    root.geometry("300x400")
    
    # Cria o 'Nome' da janela
    label = tk.Label(root, text="Soma", font=("Times New Roman", 24))
    label.pack(pady=20)
    
    # Cria os campos de entrada
    a = tk.Entry(root, font=("Arial", 16))
    a.pack(pady=5)
    b = tk.Entry(root, font=("Arial", 16))
    b.pack(pady=5) 

    def somar():
        try:
            # Obtém os valores dos campos de entrada
            valor_a = int(a.get())
            valor_b = int(b.get())
            # Calcula a soma
            resultado = valor_a + valor_b
            # Atualiza o rótulo de resultado
            label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            label_resultado.config(text="Por favor, insira números válidos.")

    # Cria o botão de soma
    button = tk.Button(root, text="Somar", font=("Times New Roman", 16), command=lambda: somar())
    button.pack(pady=20)
    
    label_resultado = tk.Label(root, text="Resultado", font=("Times New Roman", 16))
    label_resultado.pack(pady=10)

    # Faz funcionar o loop
    root.mainloop()
tela()