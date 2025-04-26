import json
from statistics import mean, median, mode, StatisticsError

def coletar_dados_aluno():
    aluno = {}
    aluno['nome'] = input("Nome: ")
    aluno['ra'] = input("RA: ")
    aluno['data_nascimento'] = input("Data de nascimento (dd/mm/aaaa): ")
    aluno['turma'] = input("Turma: ")
    aluno['cpf'] = input("CPF: ")
    aluno['rg'] = input("RG: ")

    notas = []
    qtd_notas = int(input("Quantas notas deseja inserir? "))
    for i in range(qtd_notas):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    aluno['notas'] = notas
    aluno['media'] = mean(notas)
    aluno['mediana'] = median(notas)

    try:
        aluno['moda'] = mode(notas)
    except StatisticsError:
        aluno['moda'] = "Sem moda definida"

    return aluno

# Lista para armazenar todos os alunos
lista_alunos = []

# Coleta múltiplos alunos
while True:
    print("\n=== Inserir novo aluno ===")
    aluno = coletar_dados_aluno()
    lista_alunos.append(aluno)

    continuar = input("Deseja inserir outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Salvar os dados no arquivo JSON
with open("alunos.json", "w", encoding='utf-8') as arquivo:
    json.dump(lista_alunos, arquivo, indent=4, ensure_ascii=False)

print("\n✅ Dados salvos com sucesso no arquivo 'alunos.json'!")

#....#
#teste#
