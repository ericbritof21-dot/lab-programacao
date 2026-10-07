def realizar_saque(saldo, valor_saque):
    if valor_saque <= 0:
        raise ValueError("O valor do saque deve ser positivo.")
    if valor_saque > saldo:
        raise SaldoInsuficienteError(saldo, valor_saque)
    return saldo - valor_saque
 
 
def ex12():
    saldo = 1000.0
    try:
        valor = float(input("Valor do saque: "))
        saldo = realizar_saque(saldo, valor)
    except SaldoInsuficienteError as e:
        print(f"Operação negada: {e}")
    except ValueError as e:
        print(f"Valor inválido: {e}")
    else:
        print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")
 
 