from flask import Flask, render_template_string
from pymongo import MongoClient
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco_de_dados"]
colecao = db["minha_colecao"]

@app.route('/')
def home():
    alunos = list(colecao.find({}, {"nome": 1, "peso": 1, "altura": 1, "_id": 0}))

    imcs = []
    nomes = []
    for a in alunos:
        if "peso" in a and "altura" in a and a["altura"] != 0:
            # Converte os valores de peso e altura para float antes de calcular o IMC
            peso = float(a["peso"])
            altura = float(a["altura"])
            imc = peso / (altura ** 2)
            imcs.append(imc)
            nomes.append(a["nome"])

    plt.bar(nomes, imcs)
    plt.xlabel('Nome')
    plt.ylabel('IMC')
    plt.title('IMC por Aluno')

    # Salva o gráfico em um objeto BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Converte o objeto BytesIO em uma string base64
    image = base64.b64encode(buf.read()).decode('utf-8')

    # Renderiza o template HTML com a string base64
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>IMC por Aluno</title>
    </head>
    <body>
        <h1>IMC por Aluno</h1>
        <img src="data:image/png;base64,{{ image }}">
    </body>
    </html>
    ''', image=image)

if __name__ == '__main__':
    app.run()