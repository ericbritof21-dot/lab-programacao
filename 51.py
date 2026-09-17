temperaturas = []
for i in range (5):
    temp= float(input(f"Digite a temperatura mṕdia do dai {i+1} (c°)"))
    temperaturas.append(temp)

media= sum(temperaturas) / len(temperaturas)

print (f"Temperaturas catalogadas: {temperaturas}")
print (f"Média das temperaturas: {media}")

if 18 <= media <= 28:
    print("Média dentro do ideal")
else:
    print("Média fora da faixa ideal")