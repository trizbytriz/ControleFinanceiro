import matplotlib.pyplot as plt

# Funções relacionadas ao relatório e gráfico
def gerar_relatorio(transacoes):
    receitas = sum(t[3] for t in transacoes if t[1] == "receita")
    despesas = sum(t[3] for t in transacoes if t[1] == "despesa")
    saldo = receitas - despesas

    return receitas, despesas, saldo


def gerar_grafico(receitas, despesas):
    labels = ['Receitas', 'Despesas']
    valores = [receitas, despesas]

    plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Distribuição Financeira")
    plt.show()
