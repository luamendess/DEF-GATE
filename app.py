# Bibliotecas:

from flask import Flask, jsonify, request, send_file
from tinydb import TinyDB, Query
from openpyxl import Workbook

# Rotas:

app = Flask(_name_)
db = TinyDB('db.json')

@app.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = db.table('alunos').all()
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def add_aluno():
    aluno = request.json
    db.table('alunos').insert(aluno)
    return jsonify(aluno)

@app.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    aluno = request.json
    db.table('alunos').update(aluno, Query().id == aluno_id)
    return jsonify(aluno)

@app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    db.table('alunos').remove(Query().id == aluno_id)
    return '', 204

@app.route('/alunos/download', methods=['GET'])
def download_alunos():
    wb = Workbook()
    ws = wb.active
    ws.title = 'Alunos'
    ws.append(['ID', 'Nome', 'Idade', 'Observações'])

    alunos = db.table('alunos').all()
    for aluno in alunos:
        ws.append([aluno['id'], aluno['nome'], aluno['idade'], aluno['observacoes']])

    filename = 'alunos.xlsx'
    wb.save(filename)

    return send_file(filename, as_attachment=True)

@app.route('/cursos', methods=['GET'])
def get_cursos():
    cursos = db.table('cursos').all()
    return jsonify(cursos)

@app.route('/cursos', methods=['POST'])
def add_curso():
    curso = request.json
    db.table('cursos').insert(curso)
    return jsonify(curso)

@app.route('/cursos/<int:curso_id>', methods=['PUT'])
def update_curso(curso_id):
    curso = request.json
    db.table('cursos').update(curso, Query().id == curso_id)
    return jsonify(curso)

@app.route('/cursos/<int:curso_id>', methods=['DELETE'])
def delete_curso(curso_id):
    db.table('cursos').remove(Query().id == curso_id)
    return '', 204

@app.route('/presenca', methods=['GET'])
def get_presenca():
    presenca = db.table('presenca').all()
    return jsonify(presenca)

@app.route('/presenca', methods=['POST'])
def add_presenca():
    presenca = request.json
    db.table('presenca').insert(presenca)
    return jsonify(presenca)

@app.route('/presenca/<int:presenca_id>', methods=['PUT'])
def update_presenca(presenca_id):
    presenca = request.json
    db.table('presenca').update(presenca, Query().id == presenca_id)
    return jsonify(presenca)

@app.route('/presenca/<int:presenca_id>', methods=['DELETE'])
def delete_presenca(presenca_id):
    db.table('presenca').remove(Query().id == presenca_id) 
    return'',204