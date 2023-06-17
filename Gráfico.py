from flask import Flask, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]
colecao = db["minha_colecao"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    dados_alunos = list(colecao.find())
    for aluno in dados_alunos:
        aluno['_id'] = str(aluno['_id'])  # Convertendo ObjectId para string
    return json.dumps(dados_alunos)

if __name__ == '__main__':
    app.run()