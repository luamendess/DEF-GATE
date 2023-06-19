from flask import Flask, Blueprint

# Criação dos blueprints
api1 = Blueprint('api1-Registro De Aluno', __name__)
api2 = Blueprint('api2-Registro De Professor', __name__)
api3 = Blueprint('api3-Registro De Disciplina', __name__)
api4 = Blueprint('api4-Registro De Turma', __name__)
api5 = Blueprint('api5-Gráfico De IMC', __name__)
api6 = Blueprint('api6-Consulta Dos Dados', __name__)


@app.route('/registro_de_aluno')
def api1_route():
    return "Você está no Registro De Aluno!"

@app.route('/registro_de_professor')
def api2_route():
    return "Você está no Registro De Professor!"

@app.route('/registro_de_disciplina')
def api3_route():
    return "Você está no Registro De Disciplina!"

@app.route('/registro_de_turma')
def api4_route():
    return "Você está no Registro De Turma!"

@app.route('/grafico_de_imc')
def api5_route():
    return "Você está no Gráfico De IMC!"

@app.route('/consulta_dos_dados')
def api6_route():
    return "Você está na Consulta Dos Dados!"

app = Flask(__name__)

# Registro dos blueprints
app.register_blueprint(api1, url_prefix='/api1')
app.register_blueprint(api2, url_prefix='/api2')
app.register_blueprint(api3, url_prefix='/api3')
app.register_blueprint(api4, url_prefix='/api4')
app.register_blueprint(api5, url_prefix='/api5')
app.register_blueprint(api6, url_prefix='/api6')


if __name__ == '__main__':
    app.run()