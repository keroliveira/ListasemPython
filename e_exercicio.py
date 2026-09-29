# Contabilidades

produtos = []

for _ in range(5):
    nome = input()
    preco_compra = float(input())
    percentual = float(input())
    produtos.append((nome, preco_compra, percentual))

for nome, preco_compra, percentual in produtos:
    preco_venda = preco_compra * (1 + percentual / 100)
    print(f"{nome}: Compra = R${preco_compra:.2f}, Venda = R${preco_venda:.2f}")
