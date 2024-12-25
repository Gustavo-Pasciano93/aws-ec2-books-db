import mysql.connector
import pandas as pd
from tabulate import tabulate

class MySQLHandler:
    def __init__(self, host: str, user: str, password: str, database: str = None):
        """Inicializa a conexão com o banco de dados."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.cursor = None

    def connect(self):
        """Conecta ao servidor MySQL."""
        print("Conectando ao MySQL...")
        self.cnx = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.cnx.cursor()
        print("Conexão estabelecida.")

    def show_databases(self):
        """Lista todos os bancos de dados disponíveis."""
        print("Listando bancos de dados...")
        self.cursor.execute("SHOW DATABASES")
        for db in self.cursor:
            print(db)

    def create_database(self, db_name: str):
        """Cria um banco de dados, se não existir."""
        print(f"Criando banco de dados '{db_name}' (se não existir)...")
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        self.database = db_name
        print(f"Banco de dados '{db_name}' criado ou já existente.")

    def create_table(self, table_name: str, schema: str):
        """Cria uma tabela com base no esquema fornecido."""
        print(f"Criando tabela '{table_name}' (se não existir)...")
        self.cursor.execute(schema)
        print(f"Tabela '{table_name}' criada ou já existente.")

    def insert_data(self, table_name: str, data: pd.DataFrame):
        """Insere os dados de um DataFrame na tabela."""
        print(f"Inserindo dados na tabela '{table_name}'...")
        for _, row in data.iterrows():
            sql = f"""
            INSERT INTO {table_name} (title, authors, published_date, description)
            VALUES (%s, %s, %s, %s)
            """
            values = (row["title"], row["authors"], row["published_date"], row["description"])
            self.cursor.execute(sql, values)
        self.cnx.commit()
        print("Dados inseridos com sucesso.")

    def fetch_all(self, query: str):
        """Executa uma consulta e retorna todos os resultados."""
        self.cursor.execute(query)
        return self.cursor.fetchall(), [desc[0] for desc in self.cursor.description]

    def close_cursor(self):
        """Fecha o cursor após o uso."""
        try:
            self.cursor.fetchall()  # Consome resultados pendentes, se houver
        except mysql.connector.errors.InterfaceError:
            pass
        self.cursor.close()
        print("Cursor fechado.")

    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        if self.cnx:
            self.cnx.close()
            print("Conexão com o MySQL encerrada.")

# Execução do Script
if __name__ == "__main__":
    # Inicializa a classe e conecta ao MySQL
    db_handler = MySQLHandler(host="localhost", user="gpasciano", password="Pandas@2024")
    db_handler.connect()

    # Mostra os bancos de dados disponíveis
    db_handler.show_databases()

    # Cria o banco de dados e define a tabela
    db_handler.create_database("biblioteca")
    db_handler.create_table(
        "biblioteca.tabela_livros_dados",
        """
        CREATE TABLE IF NOT EXISTS biblioteca.tabela_livros_dados(
            title VARCHAR(300),
            authors VARCHAR(300),
            published_date DATE,
            description TEXT
        )
        """
    )

    # Carrega os dados do CSV
    df = pd.read_csv("tabela_livros.csv")
    db_handler.insert_data("biblioteca.tabela_livros_dados", df)

    # Consulta os dados e exibe no formato tabular
    resultados, colunas = db_handler.fetch_all("SELECT * FROM biblioteca.tabela_livros_dados")
    print(tabulate(resultados, headers=colunas, tablefmt="psql"))

    # Fecha o cursor e a conexão
    db_handler.close_cursor()
    db_handler.close_connection()
