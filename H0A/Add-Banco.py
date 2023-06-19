# Bibliotecas usadas
from pymongo import MongoClient

# Criação de uma conexão ao MongoDB localmente
client = MongoClient("mongodb://localhost:27017/")

# Seleção do banco de dados
db = client["meu_banco_de_dados"]

# Seleção da coleção
colecao = db["minha_colecao"]

# Dados a serem inseridos
dados = {"Nome": "João Gatilho", 
         "Idade": 15, 
         "RG": "546.456.456-89", 
         "CPF": "489.456.698-78", 
         "Nome do(a) Responsável": "",
         "RG do(a) Responsável": "", 
         "CPF do(a) Responsável": "",
         "Telefone do Responsável": "", 
         "E-mail do Responsável": "", 
         "Endereço": "",
         "CEP": "",}

# Inserção dos dados
resultado = colecao.insert_one(dados)

print(f"Dados inseridos com o ID: {resultado.inserted_id}")