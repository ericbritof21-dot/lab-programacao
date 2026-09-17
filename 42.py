produção=[
    [432,234],
    [234,433]
]
total= sum(sum(linha) for linha in produção)
print(f"a soms de todos os elementos é: {total}")