notas ={
    "Eric": 10.0,
    "Gabriel": 0.0,
    "Ravel": 5.0
}
alunobuscar = input ("Digite o nome do aluno e verá sua nota: ")
if alunobuscar in notas:
    print(f"A nota de {alunobuscar} foi {notas[alunobuscar]}")
else:
    print("esse aluno não foi encontrado")
