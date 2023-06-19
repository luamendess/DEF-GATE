from flask import Flask, request, render_template_string, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]
colecao = db["minha_colecao_Turmas"]

@app.route('/')
def form():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registro de Turma Escolar</title>
    </head>
    <body>
        <h2>Formulário de Registro de Turma Escolar</h2>
        <form action="http://localhost:5000/save" method="post">
            <label for="nome_turma">Nome da Turma:</label><br>
            <input type="text" id="nome_turma" name="nome_turma" required><br>
            <label for="ano_escolar">Ano Escolar:</label><br>
            <input type="number" id="ano_escolar" name="ano_escolar" required><br>
            <label for="professor_turma">Professor da Turma:</label><br>
            <input type="text" id="professor_turma" name="professor_turma" required><br>
            <label for="numero_estudantes">Número de Estudantes:</label><br>
            <input type="number" id="numero_estudantes" name="numero_estudantes" required><br>
            <input type="submit" value="Registrar">
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