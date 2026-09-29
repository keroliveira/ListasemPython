# Ranking de Notas

nomes = []
notas = []

while True:
    nome = input().strip()
    if nome == "" or nome == "fim":
        break
    nota = float(input())
    nomes.append(nome)
    notas.append(nota)

# zip junta em pares, ordena por -nota (estável)
pares = sorted(zip(nomes, notas), key=lambda p: -p[1])

for nome, nota in pares:
    print(f"{nome}: {nota:.2f}")