# FUNCIONANDO

def sequencia_doida(a,b):

    soma = 0
    quociente = 0
    n = 2   
    m = 3

    # Aqui eu não entendi o que deveria ser feito se os numeros digitados pelo usuario não fossem compativeis com os da sequencia, entao botei que qualuqer uma das variaveis que alcançe primeiro, pararia por ali
    while n <= a or m <= b:
        quociente = n/m
        soma += quociente
        n += 1
        m += 2

    return soma

n = 0
while n <= 0:
    n = int(input("Digite o valor de n: "))
    if n <= 0:
        print("n tem que ser positivo, digite um valor novo para n!")
    else:
        break

m = int(input("Digite o valor de m: "))
print("")

resultado = sequencia_doida(n,m)
print(f"O resultado é: {resultado}")