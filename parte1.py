# Parte 1

import sqlite3 as con

# Criar tabelas
sql_clientes = '''
    CREATE TABLE IF NOT EXISTS Cliente (
    ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    RG VARCHAR (12) NOT NULL,
    Nome_Cliente VARCHAR(30) NOT NULL,
    Sobrenome_Cliente VARCHAR(40),
    Telefone VARCHAR(12),
    Rua VARCHAR(40),
    Numero VARCHAR(5),
    Bairro VARCHAR(25)
    );
'''
    
sql_produtos = '''
    CREATE TABLE IF NOT EXISTS Produto (
    ID_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Produto VARCHAR (30) NOT NULL,
    Tipo_Produto VARCHAR (25) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Qtde_Estoque SMALLINT NOT NULL
    );
'''

sql_vendas = '''
    CREATE TABLE IF NOT EXISTS Venda (
    ID_Transacao INTEGER PRIMARY KEY AUTOINCREMENT,
    Nota_Fiscal SMALLINT NOT NULL,
    ID_Cliente INTEGER NOT NULL,
    Data_Compra DATETIME,
    ID_Produto INTEGER NOT NULL,
    Quantidade SMALLINT NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
    FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID_Produto)
    );
'''

try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    cursor.execute(sql_clientes)
    cursor.execute(sql_produtos)
    cursor.execute(sql_vendas)    

    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
finally:
    if conexao:
        conexao.close()

------------------------------------------------------------------------------------------------------------------------------

# Verificar se tabelas foram criadas
import sqlite3 as con

try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    # Verificar se tabelas foram criadas
    res = cursor.execute("SELECT name FROM sqlite_master")
    print(res.fetchall())
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
finally:
    if conexao:
        conexao.close()

------------------------------------------------------------------------------------------------------------------------------

# Inserir dados na tabela Clientes
import sqlite3 as con

insere_cliente = '''
    INSERT INTO Cliente (RG, Nome_Cliente, Sobrenome_Cliente, Telefone, Rua, Numero, Bairro)
    VALUES
    ('265356325', 'Fábio', 'dos Reis', '1156326356', 'Rua do Orfanato', '235', 'Vila Prudente'),
    ('268653215', 'João', 'Cavutto', '1178563214', 'Rua do Oratório', '1957', 'Mooca'),
    ('289632457', 'Julia', 'Tamashiro', '1196323654', 'Rua Lorenzo da Viterbo', '365', 'Vila Moraes');
'''

try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    cursor.execute(insere_cliente)

    conexao.commit()    
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
else:    
    # Verificar se dados foram cadastrados
    res = cursor.execute("SELECT * FROM Cliente;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()




# Inserir dados na tabela Produtos
import sqlite3 as con

insere_produto = '''
    INSERT INTO Produto (Nome_Produto, Tipo_Produto, Preco, Qtde_Estoque) 
    VALUES
    ('Orquídea', 'Flor', 55.50, 25),
    ('Azaléa', 'Flor', 35.63, 15),
    ('Terra Vegetal', 'Insumo', 72.50, 20),
    ('Jardineira', 'Vaso', 15.50, 18);
'''

try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    cursor.execute(insere_produto)
    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
else:
    # Verificar se dados foram cadastrados
    res = cursor.execute("SELECT * FROM Produto;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()


# Inserir dados na tabela Vendas
import sqlite3 as con

insere_venda = '''
    INSERT INTO Venda (Nota_Fiscal, ID_Cliente, Data_Compra, ID_Produto, Quantidade)
    VALUES
    (123, 1, '2024-04-04', 1, 3),
    (123, 1, '2024-04-04', 2, 2),
    (124, 3, '2024-03-28', 2, 5),
    (124, 3, '2024-04-03', 3, 2),
    (124, 3, '2024-03-30', 4, 3);
'''
    
try:
    conexao = con.connect('floricultura.db')
    cursor = conexao.cursor()

    cursor.execute(insere_venda)
    conexao.commit()
except con.DatabaseError as erro:
    print("Erro no banco de dados", erro)
else:
    # Verificar se dados foram cadastrados
    res = cursor.execute("SELECT * FROM Venda;")
    print(res.fetchall())
finally:
    if conexao:
        conexao.close()
