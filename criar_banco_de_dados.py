import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('flask/usuarios.db')  # Correção na string de conexão

cursor = conn.cursor()

# Criar a tabela para armazenar os dados dos usuários
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        profissao TEXT,
        renda REAL,
        observacao TEXT
    )
''')

# Fechar a conexão com o banco de dados
conn.close()

