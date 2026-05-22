# FUNCIONANDO

lista_principal = []

N = int(input("Digite o tamanho da lista: "))

for x in range(N):
    num = int(input("Digite um número a ser adicionado: "))
    lista_principal.append(num)

def maior_comprimento(lista):

    contador = 1
    maior_seq = 1
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            contador += 1
        else:
            if contador > maior_seq:
                maior_seq = contador
                contador = 1
    
    return maior_seq 

resultado = maior_comprimento(lista_principal)
print("")
print(f"A maior sequencia tem o tamanho: {resultado}")
