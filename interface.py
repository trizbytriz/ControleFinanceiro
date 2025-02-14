import tkinter as tk
from tkinter import messagebox

from database import inserir_transacao, buscar_transacoes, criar_tabelas
from utils import gerar_relatorio, gerar_grafico


# Funções relacionadas à interface gráfica
def adicionar_transacao(tipo_var, descricao_entry, valor_entry, data_entry):
    tipo = tipo_var.get()
    descricao = descricao_entry.get()
    valor = valor_entry.get()
    data = data_entry.get()

    if not (tipo and descricao and valor and data):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
        return

    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Erro", "O valor deve ser um número!")
        return

    inserir_transacao(tipo, descricao, valor, data)
    messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")
    descricao_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)
    data_entry.delete(0, tk.END)


def mostrar_relatorio():
    transacoes = buscar_transacoes()
    receitas, despesas, saldo = gerar_relatorio(transacoes)

    relatorio_text = f"""
    === Relatório Financeiro ===
    Receitas Totais: R$ {receitas:.2f}
    Despesas Totais: R$ {despesas:.2f}
    Saldo Final: R$ {saldo:.2f}
    """

    messagebox.showinfo("Relatório Financeiro", relatorio_text)


def mostrar_grafico():
    transacoes = buscar_transacoes()
    receitas, despesas, _ = gerar_relatorio(transacoes)
    gerar_grafico(receitas, despesas)


# Configuração da interface gráfica
def iniciar_interface():
    criar_tabelas()

    root = tk.Tk()
    root.title("Controle Financeiro")

    # Variáveis da interface gráfica
    tipo_var = tk.StringVar()
    descricao_entry = tk.Entry(root)
    valor_entry = tk.Entry(root)
    data_entry = tk.Entry(root)

    # Campos de entrada
    tk.Label(root, text="Tipo (receita/despesa):").grid(row=0, column=0, padx=10, pady=5)
    tk.OptionMenu(root, tipo_var, "receita", "despesa").grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Descrição:").grid(row=1, column=0, padx=10, pady=5)
    descricao_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Valor:").grid(row=2, column=0, padx=10, pady=5)
    valor_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Data (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
    data_entry.grid(row=3, column=1, padx=10, pady=5)

    # Botões
    tk.Button(root, text="Adicionar Transação",
              command=lambda: adicionar_transacao(tipo_var, descricao_entry, valor_entry, data_entry)).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Mostrar Relatório", command=mostrar_relatorio).grid(row=5, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Mostrar Gráfico", command=mostrar_grafico).grid(row=6, column=0, columnspan=2, pady=5)

    root.mainloop()

