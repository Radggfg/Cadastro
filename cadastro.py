import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Galão", "Caixa", "Saco", "unidade"]
lista_codigos = []

# Criando a janela:

janela = tk.Tk()
janela.title("Ferramenta de cadastro de materiais")

# Criação da função
def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos) + 1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))


label_descricao = tk.Label(text="Descrição do material")
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo da unidade do material")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, columnspan=2)

label_quant = tk.Label(text="Quantidade na unidade de material")
label_quant.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky="nswe", columnspan=2)

botao_criar_codigo = tk.Button(text="Criar código", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)


janela.mainloop()

print(lista_codigos)