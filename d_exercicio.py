# Quantos pares? Quantos ímpares?

qtd_total = 0
soma_pares = 0
soma_impares = 0

numero = int(input())
qtd_total += 1

if numero % 2 == 0:
    soma_pares += numero
else:
    soma_impares += numero

confirmacao = input()
while confirmacao == 's' or confirmacao == 'S':
    numero = int(input())
    qtd_total += 1

    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

    confirmacao = input()

print(f"Quantidade de números digitados: {qtd_total}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")