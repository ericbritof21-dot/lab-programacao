import random

participantes = ["Ana","Carlos","Pedro","Beatriz","Maria"]
sort= random.randint(0, len(participantes) -1)

lider= participantes[sort]

print(f"O número sorteado foi {sort}, logo o lider de equipe é {lider}")