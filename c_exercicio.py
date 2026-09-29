# Quantos maiores que a média?

entrada = input().split()
numeros = [int(x) for x in entrada]

media = sum(numeros) / len(numeros)

contador = sum(1 for n in numeros if n > media)

print(contador)