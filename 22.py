qtdnotas = int(input("quantos alunos fizeram a prova?: "))
notas=[]
for i in range(qtdnotas):
    nota=input(f"DIgite a nota dos {qtdnotas} alunos: ")
    notas.append(nota)
print (f"a maior nota é:{max(notas)}")