# FUNCIONANDO

def somar(a,b):
    soma = a+b
    return soma

def subtrair(a,b):
    subtracao = a-b
    return subtracao

def multiplicar(a,b):
    multiplicacao = a*b
    return multiplicacao

def dividir(a,b):
    divisao = a/b
    return divisao

def interface_calculadora():

    print("Calculadora")
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    print("")
    operacao = input("Agora digite o simbolo de qual operação gostaria de realizar (+ - * /): ")

    if operacao == "+":
        resposta = somar(n1,n2)
        return print(resposta)
    elif operacao == "-":
        resposta = subtrair(n1,n2)
        return print(resposta)
    elif operacao == "*":
        resposta = multiplicar(n1,n2)
        return print(resposta)
    elif operacao == "/":
        resposta = dividir(n1,n2)
        return print(resposta)
    else:
        return print("Não foi possivel realizar a operação, tente novamente e digite um simbolo válido")


interface_calculadora()