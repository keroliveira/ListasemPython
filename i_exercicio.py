# Listinha de compras

itens = []

while True:
    item = input()
    if item.lower() == "fim":
        break
    itens.append(item)

itens.sort(key=str.lower)

for item in itens:
    print(item)