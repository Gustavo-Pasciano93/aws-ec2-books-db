import requests
import pandas as pd

class BookDataExtractor:
    def __init__(self, query: str, max_results: int = 10):
        self.url = "https://www.googleapis.com/books/v1/volumes"
        self.query = query
        self.max_results = max_results
        self.books = []
        self.data = None

    def fetch_data(self):
        """Faz a requisição à API e armazena os dados."""
        print("Fazendo requisição à API...")
        parametros = {"q": self.query, "maxResults": self.max_results}
        response = requests.get(self.url, parametros)
        response.raise_for_status()  # Garante que erros HTTP sejam tratados
        self.data = response.json().get("items", [])
        print(f"Dados obtidos com sucesso: {len(self.data)} registros encontrados.")

    def process_data(self):
        """Processa os dados obtidos e os transforma em uma lista de dicionários."""
        print("Processando os dados...")
        if not self.data:
            raise ValueError("Nenhum dado para processar. Execute 'fetch_data' primeiro.")
        
        for item in self.data:
            self.books.append({
                "title": item["volumeInfo"].get("title", "Sem título"),
                "authors": ", ".join(item["volumeInfo"].get("authors", ["Desconhecido"])),
                "published_date": item["volumeInfo"].get("publishedDate", None),
                "description": item["volumeInfo"].get("description", "Sem descrição")
            })
        print(f"Dados processados com sucesso: {len(self.books)} registros preparados.")

    def save_to_csv(self, filename: str):
        """Salva os dados em um arquivo CSV."""
        print(f"Salvando os dados no arquivo '{filename}'...")
        if not self.books:
            raise ValueError("Nenhum dado para salvar. Execute 'process_data' primeiro.")
        
        df = pd.DataFrame(self.books)
        df.to_csv(filename, index=False)
        print(f"Arquivo '{filename}' salvo com sucesso.")

# Execução do Script
if __name__ == "__main__":
    extractor = BookDataExtractor(query="data engineering", max_results=10)
    extractor.fetch_data()
    extractor.process_data()
    extractor.save_to_csv("tabela_livros.csv")
