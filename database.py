import sqlite3

# Conectar ao banco de dados ou criar se não existir
conn = sqlite3.connect('cadastros.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        senha TEXT,
        telefone TEXT
    )
''')

# Função para inserir um cadastro no banco de dados
def inserir_cadastro(nome, email, senha, telefone):
    cursor.execute('INSERT INTO cadastros (nome, email, senha, telefone) VALUES (?, ?, ?, ?)', (nome, email, senha, telefone))
    conn.commit()

# Fechar a conexão com o banco de dados
def fechar_conexao():
    conn.close()
