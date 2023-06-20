# Bibliotecas usadas
from pymongo import MongoClient

# Criação de uma conexão ao MongoDB localmente
client = MongoClient("mongodb://localhost:27017/")

# Seleção do banco de dados
db = client["meu_banco_de_dados"]

# Seleção da coleção
colecao = db["minha_colecao"]

# Dados a serem inseridos
dados = {"Nome": "Ricardo", 
         "Idade": 6, 
         "RG": "00.000.000-0", 
         "CPF": "000.000.000-00", 
         "Nome do(a) Responsável": "Róger",
         "RG do(a) Responsável": "00.000.000-0", 
         "CPF do(a) Responsável": "000.000.000-00",
         "Telefone do Responsável": "(11) 0000-0000", 
         "E-mail do Responsável": "RogerPik4demetal@gmail.com", 
         "Endereço": "Casa do caralho, 062",
         "CEP": "25791-444",}

# Inserção dos dados
resultado = colecao.insert_one(dados)

print(f"Dados inseridos com o ID: {resultado.inserted_id}")