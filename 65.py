def calcularCubo(n):
    return n ** 3

def calcularcubo(n):
    return calcularCubo(n)

def calcularDivisaoCubo(n):
    if n % 3 == 0:
        return calcularCubo(n)
    return False

print(calcularCubo(3))          # 27
print(calcularDivisaoCubo(6))  # 216
print(calcularDivisaoCubo(5))  # False