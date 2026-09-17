alunos={}
for i in range(5):
    nome= input(f"Digite o nome do aluno {i+1}: ")
    nota= float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota  # <-- ESSA LINHA FALTAVA! (Guarda a chave e o valor)

for nome, nota in alunos.items():
    print(f"Aluno: {nome} | Nota: {nota:.1f}")