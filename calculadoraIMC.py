# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Solicita ao usuário que insira seu peso e altura
peso = float(input("Insira seu peso em quilogramas: "))
altura = float(input("Insira sua altura em metros: "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Imprime o IMC
print("Seu Índice de Massa Corporal é: ", imc)
