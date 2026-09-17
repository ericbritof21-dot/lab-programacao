import random
numerochute= int(input("Digite um número de 1 a 10: "))
numerosor=random.randint(1,10)
if numerochute == numerosor:
    print("Parábens você acertou!")
else:
    print(f"Você errou,o número era {numerosor},tente outra vez")

