cadastro={
    "produto": input("Digite qual propduto deseja adicionar: "),
    "valor": float(input("Digite qual o valor do seu produto em R$: ")),
    "quantidade": int(input("Qual a quantidade em estoque desse produto?: "))
}

print(f"o produto cadastrado foi {cadastro['produto']} e a sua quantidade é {cadastro['quantidade']}")
