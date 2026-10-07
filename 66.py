def galinhas_e_coelhos(cabecas, pernas):
    """
    g + c = cabecas
    2g + 4c = pernas  ->  c = (pernas - 2*cabecas) / 2
    """
    coelhos = (pernas - 2 * cabecas) / 2
    galinhas = cabecas - coelhos
 
    if coelhos < 0 or galinhas < 0 or coelhos != int(coelhos):
        raise ValueError("Não existe solução válida para esses valores.")
    return int(galinhas), int(coelhos)
 
 
def ex01():
    try:
        g, c = galinhas_e_coelhos(35, 94)
        print(f"Galinhas: {g} | Coelhos: {c}")
    except ValueError as e:
        print(e)
 