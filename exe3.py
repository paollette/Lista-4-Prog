# FUNCIONANDO

vetor = []

print("Criando o vetor de 20 posições+")

for x in range(20):
    num = int(input("Digite um número para ser adicionado no vetor: "))
    vetor.append(num)

def alterando_vetor(lista):

    lista_alterada = []

    for elemento in lista:
        if elemento < 0:
            lista_alterada.append(0)
        elif elemento < 10 and elemento >= 0:
            lista_alterada.append(1)
        else:
            lista_alterada.append(2)

    return lista_alterada

resultado = alterando_vetor(vetor)
print(resultado)
        