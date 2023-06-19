from flask import Flask, request, render_template_string
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from pymongo import MongoClient

app = Flask(__name__)

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]
colecao = db["minha_colecao_imc_dos_alunos"]

@app.route('/', methods=['GET', 'POST'])
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
            colecao.insert_one({"nome": nome, "peso": peso, "altura": altura, "imc": imc})

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

        alunos = list(colecao.find())

        return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>IMC por Aluno</title>
        </head>
        <body>
            <h1>IMC por Aluno</h1>
            <img src="data:image/png;base64,{{ image }}">
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
        </body>
        </html>
        ''', image=image, alunos=alunos)

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registro de Alunos</title>
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
        <Peço desculpas pela resposta anterior ter sido cortada. Aqui está a continuação do código:

```python
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

if __name__ == '__main__':
    app.run()