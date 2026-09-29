# Números elevados a expoente

numeros = []
for _ in range(10):
    numeros.append(float(input()))

expoente = int(input())

elevados = [n ** expoente for n in numeros]

for valor in elevados:
    print(f"{valor:.2f}")