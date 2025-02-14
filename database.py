import sqlite3

# Funções relacionadas ao banco de dados
def criar_tabelas():
    conn = sqlite3.connect("financeiro.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,          -- 'receita' ou 'despesa'
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()


def inserir_transacao(tipo, descricao, valor, data):
    conn = sqlite3.connect("financeiro.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transacoes (tipo, descricao, valor, data) VALUES (?, ?, ?, ?)",
                   (tipo, descricao, valor, data))
    conn.commit()
    conn.close()


def buscar_transacoes():
    conn = sqlite3.connect("financeiro.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transacoes ORDER BY data")
    transacoes = cursor.fetchall()
    conn.close()
    return transacoes

