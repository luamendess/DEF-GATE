# Bibliotecas usadas
from flask import Flask, jsonify, request, make_response
from pymongo import MongoClient
import pandas as pd

# Criação de uma conexão ao MongoDB localmente
client = MongoClient("mongodb://localhost:27017/")

# Seleção do banco de dados
db = client["meu_banco_de_dados"]

# Seleção da coleção
colecao = db["minha_colecao"]

# Dados a serem inseridos
dados = {"nome": "João", "idade": 30}

# Inserção dos dados
resultado = colecao.insert_one(dados)

print(f"Dados inseridos com o ID: {resultado.inserted_id}")