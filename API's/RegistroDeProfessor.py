from flask import Flask, request, render_template_string, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]
colecao = db["minha_colecao_professores"]

@app.route('/prof')
def form():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contratação de Professor</title>
    </head>
    <body>
        <h1>Contratação de Professor</h1>
    
    <form action="/save_prof" method="POST">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br><br>
        
        <label for="idade">Idade:</label>
        <input type="text" id="idade" name="idade" required><br><br>
        
        <label for="especialidade">Especialidade:</label>
        <input type="text" id="especialidade" name="especialidade" required><br><br>
        
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="telefone">Telefone:</label>
        <input type="tel" id="telefone" name="telefone" required><br><br>
        
        <label for="cpf">CPF:</label>
        <input type="text" id="cpf" name="cpf" required><br><br>
        
        <label for="rg">RG:</label>
        <input type="text" id="rg" name="rg" required><br><br>
        
          <label for="endereço">Endereço:</label>
        <input type="text" id="endereço" name="endereço" required><br><br>
        
          <label for="cep">CEP:</label>
        <input type="text" id="cep" name="cep" required><br><br>
        
        <input type="submit" value="Contratar">

        </form>
    </body>
    </html>
    ''')

@app.route('/save_prof', methods=['POST'])
def save_prof():
    data = request.form.to_dict()
    resultado = colecao.insert_one(data)
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contratado(a)</title>
    </head>
    <body>
        <h2>Dados inseridos com o ID: {{resultado.inserted_id}}</h2>
        <button onclick="window.location.href='/'">Voltar</button>
    </body>
    </html>
    ''', resultado=resultado)

if __name__ == '__main__':
    app.run()
