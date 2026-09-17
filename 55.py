disciplinas = ("Matemática", "Português")
alunos={}

qtdalunos= int(input("Quantos alinos deseja cadastrar?: "))
for i in range (qtdalunos):
    nome= input(f"Digite o nome do aluno{i+1}: ")
    notam= float(input(f"Qual a nota de {nome} em matemática?: "))
    notap= float(input(f"Qual a nota de {nome} em portugues?: "))
    alunos[nome]= {
        disciplinas[0]: notam,
        disciplinas[1]: notap
    }
for nome, notas in alunos.items():
    media = (notas[disciplinas[0]] + notas[disciplinas[1]])/2

    if media >= 7.0:
        desempenho="Aprovado"
    else:
        desempenho="Reprovado"
print(f"Aluno: {nome} |Média: {media}|Desempenho: {desempenho}")


             
