import tkinter as tk
from tkinter import messagebox

def clicar_botao(valor):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(valor))

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Erro", "Cálculo Inválido")
        limpar()

# Configuração da Janela
janela = tk.Tk()
janela.title("Calculadora Pro")
janela.geometry("300x420")
janela.configure(bg="#2c3e50") # Cor de fundo da janela (Azul Petróleo Escuro)

# Campo de entrada estilizado
entrada = tk.Entry(janela, font=("Arial", 28), bg="#34495e", fg="white", 
                  borderwidth=0, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=30, sticky="nsew")

# Dicionário de cores para os botões
estilo_botoes = {
    "padrao": {"bg": "#ecf0f1", "fg": "#2c3e50"}, # Cinza claro
    "operador": {"bg": "#e67e22", "fg": "white"}, # Laranja
    "especial": {"bg": "#95a5a6", "fg": "white"}  # Cinza médio
}

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

linha = 1
coluna = 0

for botao in botoes:
    # Define a cor baseada no tipo de botão
    if botao in ('/', '*', '-', '+', '='):
        cor = estilo_botoes["operador"]
    elif botao == 'C':
        cor = estilo_botoes["especial"]
    else:
        cor = estilo_botoes["padrao"]

    # Criando o botão com as cores definidas
    comando = calcular if botao == '=' else limpar if botao == 'C' else lambda b=botao: clicar_botao(b)
    
    tk.Button(janela, text=botao, width=5, height=2, font=("Arial", 14, "bold"),
              bg=cor["bg"], fg=cor["fg"], relief="flat", activebackground="#bdc3c7",
              command=comando).grid(row=linha, column=coluna, padx=3, pady=3, sticky="nsew")
    
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Faz as colunas e linhas crescerem proporcionalmente
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()
