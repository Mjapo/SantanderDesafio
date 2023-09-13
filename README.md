# SatanderDesafio


# Satander DEV


# ETL para Inserção de Usuários e Geração de CSV

Este é um projeto de ETL (Extração, Transformação e Carga) que permite a inserção de dados de usuários em um banco de dados SQLite(`clientes2.db`) ele carrega os dados pelo `app.py` que insere os usarios e cria um arquivo `usuarios.csv` . apos esse processo .voce pode entrar no arquivo  `analise.ipynb` que vai alimentar o html `table.html `. para voce visualizar os dados pelo `html ` pelo terminal vá ate o terminal  digite o comando `cd flask` e digite `python .\main.py` vai abrir um localhost: `http://127.0.0.1:5000` vai abrir uma pagina `listar_usuarios.html` que vai ter um botao para direcionar a pagina `table.html ` . 


## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.912
- SQLite ( Python)  
- Biblioteca `sqlite3` ( Python)
- Biblioteca `json` ( Python)
- Biblioteca `csv` (Python)
- Biblioteca `flask` (Python)
- Biblioteca `from IPython.display import display, HTML, FileLink` - Python 

## Como Usar

1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Execute o arquivo `criar_banco_de_dados.py` para criar o banco de dados SQLite:
 ele vai criar o banco de dados do sqllite dentro da pasta flask `lembre-se de renomea-lo `

```
python criar_banco_de_dados.py
```

1. Edite o arquivo `mensagem.json` para adicionar ou modificar as mensagens que serão associadas aos usuários.

2. Execute o arquivo `app.py` para inserir novos usuários no banco de dados e gerar um arquivo CSV:
   e vai te permitir construir um arquivo CSV , que sera carregado a uma pasta copia flask que te mostrar os dados inseridos 

   - crie um nomo de `arquivo.csv`
   - coloque o nome do banco de dados que foi criado `clientes2.db`
   - preencha os usuarios a serem inseridos `ID, NOME , IDADE ,PROFISSAO ,RENDA E MENSAGEM`
   - Apos isso rode  o `app.py`
   - esse codigo vai alimenatar o banco de dados e vai criar um arquivo ou alimentar o arqwuivo csv
   - agora feito este passo , va para o arquivo `analise.ipynb` e rode os  comandos da etapa do codigo 
   - quando chegar neste comando :




# Transformar os dados em uma tabela HTML com estilos CSS inline
html_table = df.to_html(classes='table', escape=False, index=False, table_id='my-table')

# Obter o diretório atual
current_dir = os.getcwd()

# Caminho para a pasta 'template' dentro do diretório atual
template_path = os.path.join(current_dir, 'flask', 'static')

# Verificar se a pasta 'template' existe, senão, crie-a
if not os.path.exists(template_path):
    os.makedirs(template_path)

# Abra o arquivo table.html para escrever o conteúdo
with open(os.path.join(template_path, 'table.html'), 'w', encoding='utf-8') as file:
    file.write('<html><head>')
    file.write('<style>')
    file.write('.table { border-collapse: collapse; width: 100%; }')
    file.write('.table, th, td { border: 5px solid black; padding: 8px; }')
    file.write('.center { text-align: center; }')  # Estilo CSS para centralizar
    file.write('</style>')
    file.write('</head><body>')

    # Centralize o título
    file.write('<h1 class="center">Minha Tabela de Usuários</h1>')




    # Inserir a tabela gerada
    file.write(html_table)

    file.write('</body></html>')

    - ele vai alimentar o conteudo `table.html` ou criar uma nova tabela 



- agora voce vai entrar na pasta `cd  flask ` . 
- de um `ls` para checar se esta na pasta flask   e consegue visualizar o arquivo `main.py` 
- no terminal coloque o comando `python .\main.py` . isso vai rodar uma aplicacao no flask e abrir um localhost 
- vai abrir a listar_usuarios.html e vai conterm um link 
- para a table.html 



## Adicionando Novos Usuários

Para adicionar novos usuários, basta editar a lista `lista_usuarios` no arquivo `app.py`. Adicione os novos usuários no formato `(ID, Nome, Idade, Profissão, Renda)` na lista.


## Notas Adicionais

- O arquivo `clientes2.db` contém o banco de dados SQLite onde os dados dos usuários são armazenados.
- Sempre verifique se você tem as bibliotecas Python necessárias instaladas em seu ambiente local.


## Nota :

voce pode rodar o codigo local  ou criar novos usuarios ,id , renda , profissao e mensagem .mas sempre altere as rotas locais e sigas os processos das etapas 



### Marcelo ishida takeya
