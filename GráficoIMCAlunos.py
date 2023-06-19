import matplotlib.pyplot as plt

# Lista de pessoas com peso e altura
pessoas = [
    {"nome": "João", "peso": 300, "altura": 1.90},
    {"nome": "Maria", "peso": 60, "altura": 1.68},
    {"nome": "Carlos", "peso": 70, "altura": 1.80},
    # Adicione mais pessoas conforme necessário
]

# Calcula o IMC para cada pessoa e armazena em uma lista
imcs = [p["peso"] / (p["altura"] ** 2) for p in pessoas]

# Cria uma lista com os nomes para usar como rótulos no eixo x
nomes = [p["nome"] for p in pessoas]

# Cria um gráfico de barras com os IMCs
plt.bar(nomes, imcs)
plt.xlabel('Nome')
plt.ylabel('IMC')
plt.title('IMC por Pessoa')
plt.show()