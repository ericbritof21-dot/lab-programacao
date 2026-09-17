import random
numerosort= random.randint(1,10)
while True:
    numerochute= int(input("Digite um número de 1 a 10: "))
    if numerochute < 1 or numerochute > 10:
        print(f"O número {numerochute} não está entre 1 e 10. Tente novamente!")
    elif numerochute > numerosort:
        print(f"O número sorteado é MENOR que {numerochute}. Tente novamente!")
    elif numerochute < numerosort:
        print(f"O número sorteado é MAIOR que {numerochute}. Tente novamente!")
    else:
        print(f"Parabéns, você acertou!! O número era {numerosort}.")
        break