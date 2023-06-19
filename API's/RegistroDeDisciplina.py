from flask import Flask, request, render_template_string, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]
colecao = db["minha_colecao_Disciplinas"]

@app.route('/')
def form():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registro de Disciplinas Escolares</title>
    </head>
    <body>
        <h2>Formulário de Registro de Disciplinas Escolares</h2>
        <form action="http://localhost:5000/save" method="post">
            <label for="disciplina">Nome da Disciplina:</label><br>
            <input type="text" id="disciplina" name="disciplina" required><br>
            <label for="professor">Nome do Professor:</label><br>
            <input type="text" id="professor" name="professor" required><br>
            <label for="horario">Horário da Disciplina:</label><br>
            <input type="time" id="horario" name="horario" required><br>
            <label for="dias">Dias da Semana:</label><br>
            <select id="dias" name="dias" multiple required>
                <option value="segunda">Segunda-feira</option>
                <option value="terca">Terça-feira</option>
                <option value="quarta">Quarta-feira</option>
                <option value="quinta">Quinta-feira</option>
                <option value="sexta">Sexta-feira</option>
            </select><br>
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