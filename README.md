# Book Data Extractor AWS EC2

Este projeto extrai informações de livros da API Google Books e armazena esses dados em uma tabela MySQL. Utilizando requests para fazer requisições à API, pandas para manipulação dos dados e mysql-connector para interagir com o banco de dados, o sistema permite que você facilmente obtenha dados sobre livros e os armazene em seu banco de dados MySQL.

**Além disso, este projeto foi implantado em uma instância AWS EC2, marcando o meu primeiro projeto na nuvem.
---

## 🗂️ Estrutura do Projeto


---

## 🚀 Funcionalidades

- **Extração de dados:** Coleta informações de livros da API do Google Books com base em uma query personalizada.
- **Processamento de Dados:** Processa os dados e os organiza em um formato adequado para inserção no banco de dados.
- **Armazenamento MySQL:** Armazena os dados extraídos em uma tabela MySQL com as colunas title, authors, published_date, e description.
- **Criação Automática de Banco e Tabela:** O script cria o banco de dados e a tabela, caso eles ainda não existam.
- **Deploy em AWS EC2:** O projeto foi implantado em uma instância EC2 da AWS, tornando-o acessível na nuvem.
---

## 📋 Pré-requisitos

Certifique-se de ter instalado os seguintes itens antes de rodar o projeto:

- Python 3.10+
- MySQL Server
- Instância EC2 na AWS (apenas para a versão implantada na nuvem)
- Bibliotecas Python:
  - `pandas`
  - `requests`
  - `mysql-connector-python`

---

## 🛠️ Configuração

### 1. Clonar o Repositório:
git clone https://github.com/Gustavo-Pasciano93/aws-ec2-books-db
cd nome-do-repositorio


### 2. Instalar as dependências:
pip install -r requirements.txt

### 3. Configurar o Banco de Dados:
Antes de rodar os scripts, você precisará de um banco de dados MySQL. Substitua as credenciais de conexão no script mysql_handler.py:
db_handler = MySQLHandler(host="localhost", user="SEU_USUARIO", password="SUA_SENHA")

### 4. Rodar o Script Localmente ou na EC2:
Para rodar localmente:

python book_data_extractor.py


Para rodar na AWS EC2, você pode acessar a instância via SSH e executar o script diretamente na nuvem:

ssh -i "sua-chave.pem" ec2-user@ec2-seu-ip.compute.amazonaws.com
python book_data_extractor.py



---

## 📊 Estrutura de Banco de Dados

O script cria uma tabela MySQL chamada tabela_livros_dados com a seguinte estrutura:

CREATE TABLE IF NOT EXISTS biblioteca.tabela_livros_dados(
    title VARCHAR(300),
    authors VARCHAR(300),
    published_date DATE,
    description TEXT
)

## 💻 Como Funciona

### 1. Classe BookDataExtractor:
- Faz a requisição à API do Google Books.
- Processa os dados recebidos e os organiza.
- Salva os dados em um arquivo CSV.

### 2. Classe MySQLHandler:  
- Conecta-se ao banco de dados MySQL.
- Cria o banco de dados e a tabela, se necessário.
- Insere os dados no banco de dados.

## ☁️ Deploy na AWS EC2
### Este projeto foi implantado em uma instância AWS EC2, permitindo que os dados sejam extraídos e processados diretamente na nuvem, sem depender de um servidor local. O processo de deploy na EC2 envolveu:

Configuração da Instância EC2: Lançamento da instância na AWS e configuração do ambiente.
Instalação do MySQL e dependências: Configuração do banco de dados MySQL na EC2 e instalação das bibliotecas necessárias para o funcionamento do projeto.
Execução do Script na Nuvem: O script foi executado diretamente na EC2, processando os dados e armazenando-os no banco de dados hospedado também na nuvem.









