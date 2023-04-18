# Importar as bibliotecas:

from flask import Flask, jsonify, request, send_file
from tinydb import TinyDB, Query
import pandas as pd
from openpyxl import Workbook

# Instância da aplicação Flask e instanciar a base de dados TinyDB:

app = Flask(__name__)
db = TinyDB('db.json')

# Rotas para a API:

@app.route('/alunos', methods=['GET', 'POST'])
def alunos():
    if request.method == 'GET':
        # retorna todos os alunos cadastrados
    elif request.method == 'POST':
        # adiciona um novo aluno
    else:
        return jsonify({'erro': 'Método inválido'}), 405


@app.route('/alunos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def aluno(id):
    if request.method == 'GET':
        # retorna um aluno específico pelo id
    elif request.method == 'PUT':
        # atualiza um aluno pelo id
    elif request.method == 'DELETE':
        # remove um aluno pelo id
    else:
        return jsonify({'erro': 'Método inválido'}), 405


@app.route('/cursos', methods=['GET', 'POST'])
def cursos():
    if request.method == 'GET':
        # retorna todos os cursos cadastrados
    elif request.method == 'POST':
        # adiciona um novo curso
    else:
        return jsonify({'erro': 'Método inválido'}), 405


@app.route('/cursos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def curso(id):
    if request.method == 'GET':
        # retorna um curso específico pelo id
    elif request.method == 'PUT':
        # atualiza um curso pelo id
    elif request.method == 'DELETE':
        # remove um curso pelo id
    else:
        return jsonify({'erro': 'Método inválido'}), 405


@app.route('/presenca', methods=['POST'])
def presenca():
    # adiciona uma nova entrada de presença:

#Implementar as funções que serão chamadas pelas rotas:

def get_alunos():
    alunos = db.all()
    return jsonify(alunos)


def add_aluno():
    aluno = request.get_json()
    db.insert(aluno)
    return jsonify({'sucesso': True})


def get_aluno(id):
    aluno = db.get(doc_id=id)
    return jsonify(aluno)


def update_aluno(id):
    aluno = request.get_json()
    db.update(aluno, doc_ids=[id])
    return jsonify({'sucesso': True})


def delete_aluno(id):
    db.remove(doc_ids=[id])
    return jsonify({'sucesso': True})


def get_cursos():
    cursos = db.all()
    return jsonify(cursos)


def add_curso():
    curso = request.get_json()
    db.insert(curso)
    return jsonify({'sucesso': True})


def get_curso(id):
    curso = db.get(doc_id=id)
    return jsonify(curso)


def update_curso(id):
    curso = request.get_json()
    db.update(curso, doc_ids=[id])
    return jsonify({'sucesso': True})


def delete_curso(id):
    db.remove(doc_ids=[id])
    
    