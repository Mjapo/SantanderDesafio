import sqlite3
import pandas as pd
import time
import json
import csv
import os

# Obtém o diretório atual do script
current_dir = os.path.dirname(__file__)

# Caminho completo para o banco de dados clientes2.db
db_path = os.path.join(current_dir, 'flask', 'clientes2.db')
# Função para interagir com a API e salvar mensagens no banco de dados e no CSV
def enviar_mensagem_economica(usuario_id, nome, idade, profissao, renda, mensagem):
    # Inserir dados no banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO cliente (id, nome, idade, profissao, renda, observacao)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (usuario_id, nome, idade, profissao, renda, mensagem))
    conn.commit()
    conn.close()


    # Caminho completo para o arquivo CSV na pasta std
    csv_file_path_std = os.path.join(current_dir, 'usuarios.csv')
    # Salvar dados no arquivo CSV na pasta std
    with open(csv_file_path_std, 'a', newline='') as csv_file_std:
        csv_writer_std = csv.writer(csv_file_std)
        csv_writer_std.writerow([usuario_id, nome, idade, profissao, renda, mensagem])

   
# Carregar mensagens do arquivo JSON
with open(os.path.join(current_dir, 'mensagem.json'), 'r') as json_file:
    mensagens_data = json.load(json_file)
    mensagens = mensagens_data['mensagens']



# Adicionando Novos usuarios 
lista_usuarios = [
    (131, 'BOB', 25, 'Analista de Dados', 4500.0),
    (132, 'Carlos', 35, 'Professor', 3800.0),
    (133, 'Eva', 28, 'Médica', 6000.0),
    (134, 'Lucas', 45, 'Advogado', 7500.0),
    # habilite aqui os usuarios 
]
for usuario in lista_usuarios:
    usuario_id, nome, idade, profissao, renda = usuario
    mensagem = mensagens[usuario_id % len(mensagens)]
    enviar_mensagem_economica(usuario_id, nome, idade, profissao, renda, mensagem)
    time.sleep(1)

    print(usuario_id, nome, idade, profissao, renda, mensagem)



# Exemplo de como excluir do Banco de dados usuário pelo ID (Descomente para usar)

#def excluir_usuario_por_id(usuario_id):
    # Caminho completo para o banco de dados
 #   db_path = os.path.join('flask', 'clientes2.db')
 #    conn = sqlite3.connect(db_path)
  #  cursor = conn.cursor()    
    # Utilize o parâmetro usuario_id para excluir o usuário com o ID fornecido
  #  cursor.execute('DELETE FROM cliente WHERE id = ?', (usuario_id,))    
   # conn.commit()
    #conn.close()
#excluir_usuario_por_id(131)



# Excluir do Arquivo CSV
#def excluir_usuario_csv(usuario_id):   
 #   csv_path = 'usuarios.csv'
    # Carregue o arquivo CSV em um DataFrame
  #  df = pd.read_csv(csv_path,encoding='ISO-8859-1')
    # Exclua o usuário com o ID fornecido do DataFrame
   # df = df[df['ID'] != int(usuario_id)]  
    # Salve o DataFrame de volta no arquivo CSV, excluindo o usuário
    #df.to_csv(csv_path, index=False)
    # Chame a função para excluir o usuário com o ID 
#excluir_usuario_csv('131')



# Exemplo de como alterar um usuário pelo ID (Descomente para usar)
# def alterar_usuario_por_id(usuario_id, nome, idade, profissao, renda, mensagem):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute('''
#         UPDATE cliente
#         SET nome=?, idade=?, profissao=?, renda=?, observacao=?
#         WHERE id=?
#     ''', (nome, idade, profissao, renda, mensagem, usuario_id))
#     conn.commit()
#     conn.close()
