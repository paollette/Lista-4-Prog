# FUNCIONANDO

def tribonacci(num):

    sequencia = []

    n1 = 1
    n2 = 1
    n3 = 2

    sequencia.append(n1)
    sequencia.append(n2)
    sequencia.append(n3)

    for i in range(num-3):
        valor = n1 + n2 + n3
        sequencia.append(valor)
        n1, n2, n3 = n2, n3, valor
    
    return sequencia

N = int(input("Digite até que número da sequência você gostaria de ver a Tribonacci: "))
resultado = tribonacci(N)

print("")
print(f"A sequência de Tribonacci em {N} casas é = {resultado}")
