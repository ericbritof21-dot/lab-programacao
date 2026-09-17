matriz=[
    [-3,-2,-1],
    [3,2,1]
]
contador= 0
for linha in matriz:
    for numero in linha:
     if numero > 0:
        contador += 1
print(f"a quantidade de números positivos é de {contador}")