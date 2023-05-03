from flask import Flask, request, jsonify, send_file
from tinydb import TinyDB, Query
import pandas as pd

app = Flask(__name__)

# Inicializa o banco de dados
db = TinyDB('db.json')

# Define as tabelas do banco de dados
estudantes_table = db.table('estudantes')
professores_table = db.table('professores')
disciplinas_table = db.table('disciplinas')
turmas_table = db.table('turmas')
notas_table = db.table('notas')
faltas_table = db.table('faltas')

# Rota para listar todos os estudantes
@app.route("/estudantes", methods=["GET"])
def get_estudantes():
    estudantes = estudantes_table.all()
    return jsonify(estudantes)

# Rota para adicionar um novo estudante
@app.route("/estudantes", methods=["POST"])
def add_estudante():
    novo_estudante = request.get_json()
    estudantes_table.insert(novo_estudante)
    return jsonify(novo_estudante), 201

# Rota para atualizar um estudante
@app.route("/estudantes/<int:estudante_id>", methods=["PUT"])
def update_estudante(estudante_id):
    estudante = estudantes_table.get(doc_id=estudante_id)
    if estudante is None:
        return jsonify({"erro": "Estudante não encontrado"}), 404

    dados_atualizados = request.get_json()
    estudantes_table.update(dados_atualizados, doc_ids=[estudante_id])
    return jsonify(estudantes_table.get(doc_id=estudante_id))

# Rota para excluir um estudante
@app.route("/estudantes/<int:estudante_id>", methods=["DELETE"])
def delete_estudante(estudante_id):
    estudantes_table.remove(doc_ids=[estudante_id])
    return jsonify({"mensagem": "Estudante excluído com sucesso"}), 200

# Rota para listar todos os professores
@app.route("/professores", methods=["GET"])
def get_professores():
    professores = professores_table.all()
    return jsonify(professores)

# Rota para adicionar um novo professor
@app.route("/professores", methods=["POST"])
def add_professor():
    novo_professor = request.get_json()
    professores_table.insert(novo_professor)
    return jsonify(novo_professor), 201

# Rota para atualizar um professor
@app.route("/professores/<int:professor_id>", methods=["PUT"])
def update_professor(professor_id):
    professor = professores_table.get(doc_id=professor_id)
    if professor is None:
        return jsonify({"erro": "Professor não encontrado"}), 404

    dados_atualizados = request.get_json()
    professores_table.update(dados_atualizados, doc_ids=[professor_id])
    return jsonify(professores_table.get(doc_id=professor_id))

# Rota para excluir um professor
@app.route("/professores/<int:professor_id>", methods=["DELETE"])
def delete_professor(professor_id):
    professores_table.remove(doc_ids=[professor_id])
    return jsonify({"mensagem": "Professor excluído com sucesso"}), 200

# Rota para listar todas as disciplinas
@app.route("/disciplinas", methods=["GET"])
def get_disciplinas():
    disciplinas = disciplinas_table.all()
    return jsonify(disciplinas)

# Rota para adicionar uma nova disciplina
@app.route("/disciplinas", methods=["POST"])
def add_disciplina():
    nova_disciplina = request.get_json()
    disciplinas_table.insert(nova_disciplina)
    return jsonify(nova_disciplina), 201

# Rota para atualizar uma disciplina
@app.route("/disciplinas/<int:disciplina_id>", methods=["PUT"])
def update_disciplina(disciplina_id):
    disciplina = disciplinas_table.get(doc_id=disciplina_id)
    if disciplina is None:
        return jsonify({"erro": "Disciplina não encontrada"}), 404

    dados_atualizados = request.get_json()
    disciplinas_table.update(dados_atualizados, doc_ids=[disciplina_id])
    return jsonify(disciplinas_table.get(doc_id=disciplina_id))

# Rota para excluir uma disciplina
@app.route("/disciplinas/<int:disciplina_id>", methods=["DELETE"])
def delete_disciplina(disciplina_id):
    disciplinas_table.remove(doc_ids=[disciplina_id])
    return jsonify({"mensagem": "Disciplina excluída com sucesso"}), 200

# Rota para listar todas as turmas
@app.route("/turmas", methods=["GET"])
def get_turmas():
    turmas = turmas_table.all()
    return jsonify(turmas)

# Rota para adicionar uma nova turma
@app.route("/turmas", methods=["POST"])
def add_turma():
    nova_turma = request.get_json()
    turmas_table.insert(nova_turma)
    return jsonify(nova_turma), 201

# Rota para atualizar uma turma
@app.route("/turmas/<int:turma_id>", methods=["PUT"])
def update_turma(turma_id):
    turma = turmas_table.get(doc_id=turma_id)
    if turma is None:
        return jsonify({"erro": "Turma não encontrada"}), 404

    dados_atualizados = request.get_json()
    turmas_table.update(dados_atualizados, doc_ids=[turma_id])
    return jsonify(turmas_table.get(doc_id=turma_id))

# Rota para excluir uma turma
@app.route("/turmas/<int:turma_id>", methods=["DELETE"])
def delete_turma(turma_id):
    turmas_table.remove(doc_ids=[turma_id])
    return jsonify({"mensagem": "Turma excluída com sucesso"}), 200

# Rota para listar todas as notas de um estudante em uma disciplina
@app.route("/notas/<int:estudante_id>/<int:disciplina_id>", methods=["GET"])
def get_notas(estudante_id, disciplina_id):
    notas = notas_table.search((Query().estudante_id == estudante_id) & (Query().disciplina_id == disciplina_id))
    return jsonify(notas)

# Rota para adicionar uma nova nota
@app.route("/notas", methods=["POST"])
def add_nota():
    nova_nota = request.get_json()
    notas_table.insert(nova_nota)
    return jsonify(nova_nota), 201

# Rota para atualizar uma nota
@app.route("/notas/<int:nota_id>", methods=["PUT"])
def update_nota(nota_id):
    nota = notas_table.get(doc_id=nota_id)
    if nota is None:
        return jsonify({"erro": "Nota não encontrada"}), 404

    dados_atualizados = request.get_json()
    notas_table.update(dados_atualizados, doc_ids=[nota_id])
    return jsonify(notas_table.get(doc_id=nota_id))

# Rota para excluir uma nota
@app.route("/notas/<int:nota_id>", methods=["DELETE"])
def delete_nota(nota_id):
    notas_table.remove(doc_ids=[nota_id])
    return jsonify({"mensagem": "Nota excluída com sucesso"}), 200

# Rota para listar todas as faltas de um estudante em uma disciplina
@app.route("/faltas/<int:estudante_id>/<int:disciplina_id>", methods=["GET"])
def get_faltas(estudante_id, disciplina_id):
    faltas = faltas_table.search((Query().estudante_id == estudante_id) & (Query().disciplina_id == disciplina_id))
    return jsonify(faltas)

# Rota para adicionar uma nova falta
@app.route("/faltas", methods=["POST"])
def add_falta():
    nova_falta = request.get_json()
    faltas_table.insert(nova_falta)
    return jsonify(nova_falta), 201

# Rota para atualizar uma falta
@app.route("/faltas/<int:falta_id>", methods=["PUT"])
def update_falta(falta_id):
    falta = faltas_table.get(doc_id=falta_id)
    if falta is None:
        return jsonify({"erro": "Falta não encontrada"}), 404

    dados_atualizados = request.get_json()
    faltas_table.update(dados_atualizados, doc_ids=[falta_id])
    return jsonify(faltas_table.get(doc_id=falta_id))

# Rota para excluir uma falta
@app.route("/faltas/<int:falta_id>", methods=["DELETE"])
def delete_falta(falta_id):
    faltas_table.remove(doc_ids=[falta_id])
    return jsonify({"mensagem": "Falta excluída com sucesso"}), 200

# Rota para gerar um relatório de notas e faltas de um estudante em uma disciplina
@app.route("/relatorio/<int:estudante_id>/<int:disciplina_id>", methods=["GET"])
def gerar_relatorio(estudante_id, disciplina_id):
    notas = notas_table.search((Query().estudante_id == estudante_id) & (Query().disciplina_id == disciplina_id))
    faltas = faltas_table.search((Query().estudante_id == estudante_id) & (Query().disciplina_id == disciplina_id))

    # Cria um DataFrame com as notas e faltas
    df_notas = pd.DataFrame(notas)
    df_faltas = pd.DataFrame(faltas)

    # Agrupa as notas por tipo e calcula a média
    df_notas = df_notas.groupby('tipo').agg({'valor': 'mean'}).reset_index()

    # Calcula o total de faltas
    total_faltas = df_faltas['quantidade'].sum()

    # Cria um arquivo Excel com o relatório
    writer = pd.ExcelWriter('relatorio.xlsx', engine='openpyxl')
    df_notas.to_excel(writer, sheet_name='Notas', index=False)
    df_faltas.to_excel(writer, sheet_name='Faltas', index=False)
    writer.save()

    # Envia o arquivo Excel como resposta
    return send_file('relatorio.xlsx', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
