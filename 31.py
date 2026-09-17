funcionario = {
    "nome": input("DIgite o nome do funcionário: "),
    "idade": int(input("Digite a idade do funcionário: ")),
    "setor": input("Digite qual o setor do funcionário: ")
}

print(f"Nome: {funcionario['nome']}")
print(f"Idade: {funcionario['idade']}")     
print(f"Setor: {funcionario['setor']}")