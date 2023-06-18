from flask import Flask, request, render_template_string
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]

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

if __name__ == '__main__':
    app.run()
