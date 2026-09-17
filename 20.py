somanotas=0
while True:
    nota = float(input("qual a sua satisfação com a empresa?"))
    if nota ==0:
        break
    somanotas =+ nota
    
print ("a soma das notas foi", somanotas )