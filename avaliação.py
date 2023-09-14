import tkinter as tk
from tkinter import messagebox

# Função para exibir a mensagem e o nome em uma nova janela
def exibir_mensagem():
    nome = nome_entry.get()
    mensagem = mensagem_text.get("1.0", "end-1c")  # Obter todo o texto do Text widget
    
    # Verifica se o usuário inseriu um nome e uma mensagem
    if nome and mensagem:
        # Cria uma nova janela
        nova_janela = tk.Toplevel(root)
        nova_janela.title("Mensagem Enviada")
        
        # Cria rótulos para exibir o nome e a mensagem
        nome_label = tk.Label(nova_janela, text="Nome: " + nome)
        mensagem_label = tk.Label(nova_janela, text="Mensagem:")
        
        # Configura a caixa de texto na nova janela para exibir a mensagem
        mensagem_text_nova = tk.Text(nova_janela, height=10, width=40)
        mensagem_text_nova.insert("1.0", mensagem)
        mensagem_text_nova.config(state="disabled")  # Torna a caixa de texto apenas de leitura
        
        # Empacota os rótulos e a caixa de texto na nova janela
        nome_label.pack()
        mensagem_label.pack()
        mensagem_text_nova.pack()
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Envio de Mensagem")

# Rótulos e campos de texto para nome e mensagem
nome_label = tk.Label(root, text="Nome:")
nome_entry = tk.Entry(root)

mensagem_label = tk.Label(root, text="Mensagem:")
mensagem_text = tk.Text(root, height=5, width=40)  # Aumentei a largura da segunda caixa de texto

# Botão de envio
enviar_button = tk.Button(root, text="Enviar", command=exibir_mensagem)

# Organiza os elementos na janela principal
nome_label.pack()
nome_entry.pack()

mensagem_label.pack()
mensagem_text.pack()

enviar_button.pack()

# Inicia o loop principal do Tkinter
root.mainloop()

# Programa feito por Marco Antonio Rocha Merett
