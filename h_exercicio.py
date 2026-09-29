# Multiplique por k

elementos = input().split()
numeros = [int(x) for x in elementos]

k = int(input())

multiplicados = [n * k for n in numeros]

print(" ".join(str(m) for m in multiplicados) + " ")