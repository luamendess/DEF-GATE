#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
from flask import Flask, request, render_template_string, redirect, url_for
from pymongo import MongoClient
import matplotlib.pyplot as plt
import base64
from io import BytesIO
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

app = Flask(__name__)

#━━━━━━━━━❮Banco❯━━━━━━━━━
client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]
colecao2 = db["minha_colecao_imc_dos_alunos"]
colecao3 = db["minha_colecao_Disciplinas"]
colecao4 = db["minha_colecao_professores"]
colecao5 = db["minha_colecao_Turmas"]
colecao6 = db["minha_colecao"]
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━


#━━━━━━━━━❮Inicio/hub❯━━━━━━━━━
@app.route('/', methods=['GET', 'POST'])
def inc():
    return render_template_string('''<!DOCTYPE html>
<html>
<head>
    <title>SADFI</title>
    <style>
        body {
            background: linear-gradient(45deg, #7300ff, cyan);
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            padding: 0;
        }

        h1 {
            margin-bottom: 50px;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            margin: 20px 0;  /* Aumenta a margem */
        }

        a {
            text-decoration: none;
            color: white;
            border: 1px solid white;
            padding: 10px 20px;
            border-radius: 5px;
            transition: background 0.3s;
        }

        a:hover {
            background: white;
            color: #7300ff;
        }
    </style>
</head>
<body>
    <h1>Qual a área que deseja acessar? </h1>
    <ul>
        <li><a href="http://127.0.0.1:5000/colecao">Coleção</a></li>
        <li><a href="http://127.0.0.1:5000/aluno">Aluno</a></li>
        <li><a href="http://127.0.0.1:5000/prof">Professor</a></li>
        <li><a href="http://127.0.0.1:5000/home">Grafico</a></li>
        <li><a href="http://127.0.0.1:5000/turma">Turma</a></li>
        <li><a href="http://127.0.0.1:5000/disciplina">Disciplina</a></li>
    </ul>
</body>
</html>
''')

#━━━━━━❮Colecao❯━━━━━━━
@app.route('/colecao', methods=['GET', 'POST'])
def colecao():
    dados = None
    if request.method == 'POST':
        nome_colecao = request.form.get('nome_colecao')
        colecao = db[nome_colecao]
        dados = list(colecao.find())
    return render_template_string('''
    <!DOCTYPE html>
<html>
<head>
    <title>Visualizar Coleção</title>
    <style>
        body {
            background: linear-gradient(45deg, #7300ff, cyan);
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            padding: 0;
        }

        h2 {
            margin-bottom: 20px;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        label, input[type=text], input[type=submit] {
            margin: 10px 0;
        }

        input[type=text], input[type=submit] {
            padding: 10px;
            border: none;
            border-radius: 5px;
        }

        input[type=submit] {
            background: white;
            color: #7300ff;
            cursor: pointer;
            transition: background 0.3s;
        }

        input[type=submit]:hover {
            background: #7300ff;
            color: white;
        }

        pre {
            background: white;
            color: #7300ff;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h2>Escolha uma Coleção</h2>
    <form action="/colecao" method="post">
        <label for="nome_colecao">Nome da Coleção:</label><br>
        <input type="text" id="nome_colecao" name="nome_colecao"><br>
        <input type="submit" value="Visualizar">
    </form>
    {% if dados %}
    <h2>Dados da Coleção</h2>
    <pre>{{ dados }}</pre>
    {% endif %}
</body>
</html>

    ''', dados=dados)

#━━━━━━❮aluno❯━━━━━━━
@app.route('/aluno')
def form_aluno():
    return render_template_string('''
    <!DOCTYPE html>
<html>
<head>
    <title>Formulário de Cadastro</title>
    <style>
        body {
            background: linear-gradient(45deg, #7300ff, cyan);
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            padding: 0;
        }

        h2 {
            margin-bottom: 20px;
        }

        form {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            align-items: flex-start;
            justify-content: center;
        }

        .form-col {
            display: flex;
            flex-direction: column;
            margin: 0 20px;
        }

        label, input[type=text], input[type=submit] {
            margin: 10px 0;
        }

        input[type=text], input[type=submit] {
            padding: 10px;
            border: none;
            border-radius: 5px;
        }

        input[type=submit] {
            background: white;
            color: #7300ff;
            cursor: pointer;
            transition: background 0.3s;
        }

        input[type=submit]:hover {
            background: #7300ff;
            color: white;
        }
    </style>
</head>
<body>
    <h2>Formulário de Cadastro</h2>
    <form action="http://localhost:5000/save_aluno" method="post">
        <div class="form-col">
            <label for="nome"> Nome:</label><br>
            <input type="text" id="nome" name="Nome"><br>
            <label for="idade">Idade:</label><br>
            <input type="text" id="idade" name="Idade"><br>
        </div>
        <div class="form-col">
            <label for="rg">RG:</label><br>
            <input type="text" id="rg" name="RG"><br>
            <label for="cpf">CPF:</label><br>
            <input type="text" id="cpf" name="CPF"><br>
        </div>
        <div class="form-col">
            <label for="nome_responsavel">Nome do(a) Responsável:</label><br>
            <input type="text" id="nome_responsavel" name="Nome do(a) Responsável"><br>
            <label for="rg_responsavel">RG do(a) Responsável:</label><br>
            <input type="text" id="rg_responsavel" name="RG do(a) Responsável"><br>
        </div>
        <div class="form-col">
            <label for="cpf_responsavel">CPF do(a) Responsável:</label><br>
            <input type="text" id="cpf_responsavel" name="CPF do(a) Responsável"><br>
            <label for="telefone_responsavel">Telefone do Responsável:</label><br>
            <input type="text" id="telefone_responsavel" name="Telefone do Responsável"><br>
        </div>
        <div class="form-col">
            <label for="email_responsavel">E-mail do Responsável:</label><br>
            <input type="text" id="email_responsavel" name="E-mail do Responsável"><br>
            <label for="endereco">Endereço:</label><br>
            <input type="text" id="endereco" name="Endereço"><br>
            <label for="cep">
            <input type="submit" value="Enviar">
        </form>
    </body>
    </html>
    ''')

@app.route('/save_aluno', methods=['POST'])
def save_aluno():
    data = request.form.to_dict()
    resultado = colecao6.insert_one(data)
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Salvo</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h2 {
                margin-bottom: 20px;
            }

            button {
                padding: 10px;
                border: none;
                border-radius: 5px;
                background: white;
                color: #7300ff;
                cursor: pointer;
                transition: background 0.3s;
            }

            button:hover {
                background: #7300ff;
                color: white;
            }
        </style>
    </head>
    <body>
        <h2>Dados inseridos com o ID: {{resultado.inserted_id}}</h2>
        <button onclick="window.location.href='/'">Voltar</button>
    </body>
    </html>
    ''', resultado=resultado)


#━━━━━━❮grafico❯━━━━━━━
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nomes = request.form.getlist('nome')
        pesos = request.form.getlist('peso')
        alturas = request.form.getlist('altura')

        imcs = []
        for nome, peso, altura in zip(nomes, pesos, alturas):
            peso = float(peso)
            altura = float(altura)
            imc = peso / (altura ** 2)

            # Inserindo os dados no MongoDB
            colecao2.insert_one({"nome": nome, "peso": peso, "altura": altura, "imc": imc})

            imcs.append(imc)

        # Criação do gráfico fora do loop
        plt.bar(nomes, imcs)
        plt.xlabel('Nome')
        plt.ylabel('IMC')
        plt.title('IMC por Aluno')

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        image = base64.b64encode(buf.read()).decode('utf-8')

        alunos = list(colecao2.find())

        return render_template_string('''
  <!DOCTYPE html>
    <html>
    <head>
        <title>IMC por Aluno</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h1, h2 {
                margin-bottom: 20px;
            }

            img {
                max-width: 100%;
                height: auto;
            }

            .content {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }

            .content-item {
                width: 45%;
            }

            table {
                border-collapse: collapse;
                margin-bottom: 20px;
                width: 100%;
            }

            th, td {
                border: 1px solid white;
                padding: 10px;
                text-align: center;
            }

            th {
                background: #7300ff;
            }
        </style>
    </head>
    <body>
        <h1>IMC por Aluno</h1>
        <br><br>
        <br><br>
        <br><br>
        <br><br>
        <br><br>
        <div class="content">
            <div class="content-item">
                <img src="data:image/png;base64,{{ image }}">
            </div>
            <div class="content-item">
                <h2>Comparativo de IMCs</h2>
                <table>
                    <tr>
                        <th>Nome</th>
                        <th>IMC</th>
                    </tr>
                    {% for aluno in alunos %}
                    <tr>
                        <td>{{ aluno['nome'] }}</td>
                        <td>{{ aluno['imc'] }}</td>
                    </tr>
                    {% endfor %}
                </table>
            </div>
        </div>
    </body>
    </html>
        ''', image=image, alunos=alunos)

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registro de Alunos</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h2 {
                margin-bottom: 20px;
            }

            .aluno {
                margin-bottom: 20px;
            }

            label, input[type=text], input[type=number], input[type=submit], button {
                margin: 10px 0;
            }

            input[type=text], input[type=number], input[type=submit], button {
                padding: 10px;
                border: none;
                border-radius: 5px;
            }

            input[type=submit], button {
                background: white;
                color: #7300ff;
                cursor: pointer;
                transition: background 0.3s;
            }

            input[type=submit]:hover, button:hover {
                background: #7300ff;
                color: white;
            }
        </style>
    </head>
    <body>
        <h2>Formulário de Registro de Alunos</h2>
        <form method="post" id="form">
            <div class="aluno">
                <label for="nome">Nome:</label><br>
                <input type="text" id="nome" name="nome"><br>
                <label for="peso">Peso (em kg):</label><br>
                <input type="number" step="0.01" id="peso" name="peso"><br>
                <label for="altura">Altura (em metros):</label><br>
                <input type="number" step="0.01" id="altura" name="altura"><br>
            </div>
            <input type="submit" value="Registrar">
        </form>
        <button id="add">Adicionar Aluno</button>
        <script>
            document.getElementById('add').addEventListener('click', function(e) {
                e.preventDefault();
                var div = document.createElement('div');
                div.className = 'aluno';
                div.innerHTML = '<label for="nome">Nome:</label><br>\
                <input type="text" id="nome" name="nome"><br>\
                <label for="peso">Peso (em kg):</label><br>\
                <input type="number" step="0.01" id="peso" name="peso"><br>\
                <label for="altura">Altura (em metros):</label><br>\
                <input type="number" step="0.01" id="altura" name="altura"><br>';
                document.getElementById('form').appendChild(div);
            });
        </script>
    </body>
    </html>
    ''')

#━━━━━━❮disciplina❯━━━━━━━

@app.route('/disciplina')
def form():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registro de Disciplinas Escolares</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h2 {
                margin-bottom: 20px;
            }

            label, input[type=text], input[type=time], select, input[type=submit] {
                margin: 10px 0;
            }

            input[type=text], input[type=time], select, input[type=submit] {
                padding: 10px;
                border: none;
                border-radius: 5px;
            }

            input[type=submit] {
                background: white;
                color: #7300ff;
                cursor: pointer;
                transition: background 0.3s;
            }

            input[type=submit]:hover {
                background: #7300ff;
                color: white;
            }
        </style>
    </head>
    <body>
        <h2>Formulário de Registro de Disciplinas Escolares</h2>
        <form action="http://localhost:5000/save_disc" method="post">
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

@app.route('/save_disc', methods=['POST'])
def save_disc():
    data = request.form.to_dict()
    resultado = colecao3.insert_one(data)
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Salvo</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h2 {
                margin-bottom: 20px;
            }

            button {
                padding: 10px;
                border: none;
                border-radius: 5px;
                background: white;
                color: #7300ff;
                cursor: pointer;
                transition: background 0.3s;
            }

            button:hover {
                background: #7300ff;
                color: white;
            }
        </style>
    </head>
    <body>
        <h2>Dados inseridos com o ID: {{resultado.inserted_id}}</h2>
        <button onclick="window.location.href='/'">Voltar</button>
    </body>
    </html>
    ''', resultado=resultado)
    
#━━━━━━❮professor❯━━━━━━━
@app.route('/prof')
def form_prof():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contratação de Professor</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h1 {
                margin-bottom: 20px;
            }

            form {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
            }

            .form-col {
                display: flex;
                flex-direction: column;
                margin: 0 20px;
            }

            label, input[type=text], input[type=email], input[type=tel], input[type=submit] {
                margin: 10px 0;
            }

            input[type=text], input[type=email], input[type=tel], input[type=submit] {
                padding: 10px;
                border: none;
                border-radius: 5px;
            }

            input[type=submit] {
                background: white;
                color: #7300ff;
                cursor: pointer;
                transition: background 0.3s;
            }

            input[type=submit]:hover {
                background: #7300ff;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>Contratação de Professor</h1>
        <form action="/save_prof" method="POST">
            <div class="form-col">
                <label for="nome">Nome:</label>
                <input type="text" id="nome" name="nome" required>
                <label for="idade">Idade:</label>
                <input type="text" id="idade" name="idade" required>
                <label for="especialidade">Especialidade:</label>
                <input type="text" id="especialidade" name="especialidade" required>
            </div>

            <div class="form-col">
                <label for="email">E-mail:</label>
                <input type="email" id="email" name="email" required>
                <label for="telefone">Telefone:</label>
                <input type="tel" id="telefone" name="telefone" required>
                <label for="cpf">CPF:</label>
                <input type="text" id="cpf" name="cpf" required>
            </div>

            <div class="form-col">
                <label for="rg">RG:</label>
                <input type="text" id="rg" name="rg" required>
                <label for="endereço">Endereço:</label>
                <input type="text" id="endereço" name="endereço" required>
                <label for="cep">CEP:</label>
                <input type="text" id="cep" name="cep" required>
            </div>

            <input type="submit" value="Contratar">
        </form>
    </body>
    </html>
    ''')

@app.route('/save_prof', methods=['POST'])
def save_prof():
    data = request.form.to_dict()
    resultado = colecao4.insert_one(data)
    return render_template_string('''
     <!DOCTYPE html>
    <html>
    <head>
        <title>Salvo</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h2 {
                margin-bottom: 20px;
            }

            button {
                padding: 10px;
                border: none;
                border-radius: 5px;
                background: white;
                color: #7300ff;
                cursor: pointer;
                transition: background 0.3s;
            }

            button:hover {
                background: #7300ff;
                color: white;
            }
        </style>
    </head>
    <body>
        <h2>Dados inseridos com o ID: {{resultado.inserted_id}}</h2>
        <button onclick="window.location.href='/'">Voltar</button>
    </body>
    </html>
    ''', resultado=resultado)
    

#━━━━━━❮turma❯━━━━━━━

@app.route('/turma')
def form_turma():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registro de Turma Escolar</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h2 {
                margin-bottom: 20px;
            }

            .content {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
            }

            .content-item {
                width: 45%;
            }

            form {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 100%;
            }

            label, input[type=text], input[type=number], input[type=submit] {
                margin: 10px 0;
            }

            input[type=text], input[type=number], input[type=submit] {
                padding: 10px;
                border: none;
                border-radius: 5px;
            }

            input[type=submit] {
                background: white;
                color: #7300ff;
                cursor: pointer;
                transition: background 0.3s;
            }

            input[type=submit]:hover {
                background: #7300ff;
                color: white;
            }
        </style>
    </head>
    <body>
        <h2>Formulário de Registro de Turma Escolar</h2>
        <div class="content">
            <div class="content-item">
                <form action="http://localhost:5000/save_turma" method="post">
                    <label for="nome_turma">Nome da Turma:</label><br>
                    <input type="text" id="nome_turma" name="nome_turma" required><br>
                    <label for="ano_escolar">Ano Escolar:</label><br>
                    <input type="number" id="ano_escolar" name="ano_escolar" required><br>
                </form>
            </div>
            <div class="content-item">
                <form action="http://localhost:5000/save_turma" method="post">
                    <label for="professor_turma">Professor da Turma:</label><br>
                    <input type="text" id="professor_turma" name="professor_turma" required><br>
                    <label for="numero_estudantes">Número de Estudantes:</label><br>
                    <input type="number" id="numero_estudantes" name="numero_estudantes" required><br>
                    <input type="submit" value="Registrar">
                </form>
            </div>
        </div>
    </body>
    </html>
    ''')

@app.route('/save_turma', methods=['POST'])
def save_turma():
    data = request.form.to_dict()
    resultado = colecao4.insert_one(data)
    return render_template_string('''
     <!DOCTYPE html>
    <html>
    <head>
        <title>Salvo</title>
        <style>
            body {
                background: linear-gradient(45deg, #7300ff, cyan);
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                padding: 0;
            }

            h2 {
                margin-bottom: 20px;
            }

            button {
                padding: 10px;
                border: none;
                border-radius: 5px;
                background: white;
                color: #7300ff;
                cursor: pointer;
                transition: background 0.3s;
            }

            button:hover {
                background: #7300ff;
                color: white;
            }
        </style>
    </head>
    <body>
        <h2>Dados inseridos com o ID: {{resultado.inserted_id}}</h2>
        <button onclick="window.location.href='/'">Voltar</button>
    </body>
    </html>
    ''', resultado=resultado)

#━━━━━━❮iniciar api❯━━━━━━━
if __name__ == '__main__':
    app.run()