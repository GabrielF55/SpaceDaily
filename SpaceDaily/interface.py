import tkinter as tk
from tkinter import messagebox

class Tarefa:
    def __init__(self, titulo, descricao, prioridade, prazo=None, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.concluida = concluida

class GerenciarTarefas:
    def __init__(self):
        self.tarefas_pendentes = []
        self.tarefas_concluidas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas_pendentes.append(tarefa)

    def marcar_como_concluida(self, tarefa):
        tarefa.concluida = True
        self.tarefas_pendentes.remove(tarefa)
        self.tarefas_concluidas.append(tarefa)

# Criar a instância da classe GerenciarTarefas
gerenciar = GerenciarTarefas()

def adicionar_tarefa():
    titulo = entry_titulo.get()
    descricao = entry_descricao.get()
    prioridade = int(entry_prioridade.get())

    tarefa = Tarefa(titulo, descricao, prioridade)
    gerenciar.adicionar_tarefa(tarefa)

    messagebox.showinfo("Tarefa Adicionada", f"Tarefa '{titulo}' adicionada com sucesso!")

def marcar_como_concluida():
    titulo = entry_titulo.get()
    tarefas_encontradas = [tarefa for tarefa in gerenciar.tarefas_pendentes if tarefa.titulo == titulo]

    if tarefas_encontradas:
        tarefa = tarefas_encontradas[0]
        gerenciar.marcar_como_concluida(tarefa)
        messagebox.showinfo("Tarefa Concluída", f"Tarefa '{titulo}' marcada como concluída.")
    else:
        messagebox.showerror("Erro", f"Tarefa '{titulo}' não encontrada.")

root = tk.Tk()
root.title("Gerenciador de Tarefas")

# Estilos
bg_color = "#f0f0f0"
label_color = "#333333"
entry_color = "#ffffff"
button_color = "#4caf50"
button_hover_color = "#45a049"
button_text_color = "#ffffff"
font = ("Helvetica", 12)

root.config(bg=bg_color)

label_titulo = tk.Label(root, text="Título:", bg=bg_color, fg=label_color, font=font)
label_titulo.grid(row=0, column=0, sticky=tk.W, padx=10, pady=(20, 5))

entry_titulo = tk.Entry(root, bg=entry_color, font=font)
entry_titulo.grid(row=0, column=1, padx=10, pady=(20, 5))

label_descricao = tk.Label(root, text="Descrição:", bg=bg_color, fg=label_color, font=font)
label_descricao.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

entry_descricao = tk.Entry(root, bg=entry_color, font=font)
entry_descricao.grid(row=1, column=1, padx=10, pady=5)

label_prioridade = tk.Label(root, text="Prioridade:", bg=bg_color, fg=label_color, font=font)
label_prioridade.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

entry_prioridade = tk.Entry(root, bg=entry_color, font=font)
entry_prioridade.grid(row=2, column=1, padx=10, pady=5)

button_adicionar = tk.Button(root, text="Adicionar Tarefa", bg=button_color, fg=button_text_color, font=font, command=adicionar_tarefa)
button_adicionar.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="we")

button_concluir = tk.Button(root, text="Marcar como Concluída", bg=button_color, fg=button_text_color, font=font, command=marcar_como_concluida)
button_concluir.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="we")

root.mainloop()


