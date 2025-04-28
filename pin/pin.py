# Importa o módulo 'json' para salvar os dados em arquivo JSON
import json

# Importa funções estatísticas para calcular média, mediana, moda e tratar erros
from statistics import mean, median, mode, StatisticsError

# Define a função para coletar os dados de um aluno
def coletar_dados_aluno():
    aluno = {}  # Cria um dicionário vazio para armazenar os dados do aluno

    # Coleta informações básicas do aluno
    aluno['nome'] = input("Nome: ")
    aluno['ra'] = input("RA: ")
    aluno['data_nascimento'] = input("Data de nascimento (dd/mm/aaaa): ")
    aluno['turma'] = input("Turma: ")
    aluno['cpf'] = input("CPF: ")
    aluno['rg'] = input("RG: ")

    notas = []  # Cria uma lista vazia para armazenar as notas
    qtd_notas = int(input("Quantas notas deseja inserir? "))  # Pergunta quantas notas serão inseridas

    # Loop para coletar cada nota
    for i in range(qtd_notas):
        nota = float(input(f"Nota {i+1}: "))  # Solicita a nota e converte para float
        notas.append(nota)  # Adiciona a nota à lista de notas

    aluno['notas'] = notas  # Armazena a lista de notas no dicionário do aluno
    aluno['media'] = mean(notas)  # Calcula a média das notas e armazena
    aluno['mediana'] = median(notas)  # Calcula a mediana das notas e armazena

    # Tenta calcular a moda das notas
    try:
        aluno['moda'] = mode(notas)  # Calcula a moda (nota que mais aparece)
    except StatisticsError:
        aluno['moda'] = "Sem moda definida"  # Caso não tenha moda, define mensagem padrão

    return aluno  # Retorna o dicionário do aluno preenchido

# Cria uma lista vazia para armazenar todos os alunos
lista_alunos = []

# Loop principal para coletar vários alunos
while True:
    print("\n=== Inserir novo aluno ===")
    aluno = coletar_dados_aluno()  # Chama a função para coletar dados de um aluno
    lista_alunos.append(aluno)  # Adiciona o aluno à lista de alunos

    continuar = input("Deseja inserir outro aluno? (s/n): ").strip().lower()  # Pergunta se quer adicionar outro aluno
    if continuar != 's':  # Se não for 's', sai do loop
        break

# Abre (ou cria) um arquivo chamado 'alunos.json' para escrita, com codificação UTF-8
with open("alunos.json", "w", encoding='utf-8') as arquivo:
    # Salva a lista de alunos no arquivo, formatando com identação e permitindo acentos
    json.dump(lista_alunos, arquivo, indent=4, ensure_ascii=False)

# Mensagem final informando que os dados foram salvos
print("\n✅ Dados salvos com sucesso no arquivo 'alunos.json'!")
