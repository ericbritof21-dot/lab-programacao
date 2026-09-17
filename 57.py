def contar_caractere_direto(texto, caractere):
    quantidade = texto.count(caractere)
    print(f"O caractere '{caractere}' aparece {quantidade} vez(es) na string.")
contar_caractere_direto("banana", "a")