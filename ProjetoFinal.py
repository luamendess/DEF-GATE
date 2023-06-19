import subprocess

# Lista de arquivos Python (APIs)
apis = ["API's\ConexaoHTML.py", "API's\DadoAlunoGrafico.py", "API's\GraficoIMCAlunos.py", "API's\RegistroDeAluno.py",
        "API's\RegistroDeDisciplina.py", "API's\RegistroDeProfessor.py", "API's\RegistroDeTurma.py"]

while True:
    print('-='*10)
    print('1 - Consulta de Dados')
    print('2 - Registrar IMC de Aluno')
    print('3 - Grafico IMC')
    print('4 - Matricula de Aluno')
    print('5 - Registrar Disciplina')
    print('6 - Contratar Professor')
    print('7 - Registro de Turma')
    print('0 - Encerrar Operações')
    print('-='*10)
    print('')
    print("Selecione a API que deseja iniciar:")
    
    for i, api in enumerate(apis, start=1):
        print(f"{i}. {api}")
    choice = int(input("Digite o número da API: "))
    
    if choice == 0:
        break

    # Inicia o arquivo Python selecionado
    subprocess.Popen(["python", apis[choice-1]])  # Subtrai 1 aqui para corrigir o índice
