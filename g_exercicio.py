# k-ésimo maior valor

t = int(input())

numeros = []

for _ in range(t):
    numeros.append(int(input()))

k = int(input())

numeros.sort()

print(numeros[k])