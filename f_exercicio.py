# Quantidade de elementos

numeros = []

n = float(input())
numeros.append(n)

confirmacao = input()
while confirmacao == 's' or confirmacao == 'S':
    n = float(input())
    numeros.append(n)
    confirmacao = input()

ja_exibidos = []

for elemento in numeros:
    if elemento not in ja_exibidos:
        quantidade = numeros.count(elemento)
        print(f"O elemento {elemento} aparece {quantidade} vezes na lista")
        ja_exibidos.append(elemento)