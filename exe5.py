# FUNCIONANDO

def indice_elemento(lista,x):

    resultados = []
    menor_valor = lista[x]
    pulo = len(lista[:x])
    corte = lista[x:]
    indice_mv = 0

    for j in range(len(corte)-1):
        if corte[j+1] < menor_valor:
            menor_valor = corte[j+1]
            indice_mv = (j+1)+pulo

    resultados.append(menor_valor)
    resultados.append(indice_mv)

    return resultados


lista_B = []

N = int(input("Digite o tamanho da lista que gostaria de adicionar: "))
for i in range(N):
    num = int(input("Digite o valor que gostaria de adicionar a lista: "))
    lista_B.append(num)
K = int(input("Digite o indice para fazer a busca: "))

resultado = indice_elemento(lista_B,K)
print("")
print(f"Com a lista {lista_B} e K = {K} --> Indice {resultado[1]}, elemento {resultado[0]}")

