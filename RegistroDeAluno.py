from flask import Flask, request, render_template_string, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]
colecao = db["minha_colecao"]

@app.route('/')
def form():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Formulário de Cadastro</title>
    </head>
    <body>
        <h2>Formulário de Cadastro</h2>
        <form action="http://localhost:5000/save" method="post">
        <label for="nome"> Nome:</label><br>
        <input type="text" id="nome" name="Nome"><br>
        <label for="idade">Idade:</label><br>
        <input type="text" id="idade" name="Idade"><br>
        <label for="rg">RG:</label><br>
        <input type="text" id="rg" name="RG"><br>
        <label for="cpf">CPF:</label><br>
        <input type="text" id="cpf" name="CPF"><br>
        <label for="nome_responsavel">Nome do(a) Responsável:</label><br>
        <input type="text" id="nome_responsavel" name="Nome do(a) Responsável"><br>
        <label for="rg_responsavel">RG do(a) Responsável:</label><br>
        <input type="text" id="rg_responsavel" name="RG do(a) Responsável"><br>
        <label for="cpf_responsavel">CPF do(a) Responsável:</label><br>
        <input type="text" id="cpf_responsavel" name="CPF do(a) Responsável"><br>
        <label for="telefone_responsavel">Telefone do Responsável:</label><br>
        <input type="text" id="telefone_responsavel" name="Telefone do Responsável"><br>
        <label for="email_responsavel">E-mail do Responsável:</label><br>
        <input type="text" id="email_responsavel" name="E-mail do Responsável"><br>
        <label for="endereco">Endereço:</label><br>
        <input type="text" id="endereco" name="Endereço"><br>
        <label for="cep">CEP:</label><br>
        <input type="text" id="cep" name="CEP"><br>
        <input type="submit" value="Enviar">
        </form>
    </body>
    </html>
    ''')

@app.route('/save', methods=['POST'])
def save():
    data = request.form.to_dict()
    resultado = colecao.insert_one(data)
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Salvo</title>
    </head>
    <body>
        <h2>Dados inseridos com o ID: {{resultado.inserted_id}}</h2>
        <button onclick="window.location.href='/'">Voltar</button>
    </body>
    </html>
    ''', resultado=resultado)

if __name__ == '__main__':
    app.run()