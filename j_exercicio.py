# Palavras que começam com vogalvogais

vogais = []

while True:
    palavra = input()
    if palavra == "fim":
        break
    if palavra[0].lower() in "aeiou":
        vogais.append(palavra)

if len(vogais) == 0:
    print("Nenhuma palavra digitada começa com vogal.")
else:
    for palavra in vogais:
        print(palavra)