def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

alunos = []

for i in range(30):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for j in range(5):
        nota = float(input(f"Digite a {j+1}ª nota de 0 a 10: "))
        while nota < 0 or nota > 10:
            nota = float(input("Nota inválida! Digite uma nota de 0 a 10: "))
        notas.append(nota)
    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)
    alunos.append((nome, media, situacao))

print("\nLista de alunos aprovados:")
for aluno in alunos:
    if aluno[2] == "Aprovado":
        print(f"Nome: {aluno[0]} - Média: {aluno[1]} - Situação: {aluno[2]}")