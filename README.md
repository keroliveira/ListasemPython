# 🐍 Exercícios de Listas em Python

Repositório com exercícios de Python focados em listas: criação, manipulação, ordenação, filtragem, list comprehension, tuplas e formatação de saída.

## Índice
[a) Números elevados a expoente]
[b) Ranking de notas]
[c) Quantos maiores que a média?]
[d) Quantos pares? Quantos ímpares?]
[e) Contabilidades]
[f) Quantidade de elementos]
[g) k-ésimo maior valor]
[h) Multiplique por k]
[i) Listinha de compras]
[j) Palavras que começam com vogal]

## a) Números elevados a expoente:
Lê 10 números e um expoente, e exibe cada número elevado ao expoente com duas casas decimais. Primeiro contato com listas: criação, `append` e list comprehension como forma compacta de transformar todos os elementos de uma lista de uma vez.

## b) Ranking de notas:
Lê nome e nota de vários alunos até "fim" (ou nome vazio) e exibe os alunos ordenados da maior para a menor nota. Trabalha **ordenação estável** — empates mantêm a ordem de entrada — usando `key=lambda p: -p[1]` em vez de `reverse=True`, que inverteria a ordem dos empates.

## c) Quantos maiores que a média?:
Recebe uma lista de inteiros em uma única linha, calcula a média aritmética e conta quantos elementos são maiores que ela. Exercita `input().split()`, conversão com `map(int, ...)`, média com divisão real (`/`) e contagem condicional com `sum(1 for ... if ...)`.

## d) Quantos pares? Quantos ímpares?:
Lê números inteiros até o usuário não querer mais (confirmação `s`/`S`), e exibe a quantidade total, a soma dos pares e a soma dos ímpares. Trabalha o padrão `while True` + `break` para simular `do-while` e o operador `%` para distinguir par de ímpar.

## e) Contabilidades:
Lê nome, preço de compra e percentual de lucro de 5 produtos e exibe, para cada um, o preço de venda calculado. Introduz **lista de tuplas** e **desempacotamento no `for`** como alternativa robusta a listas paralelas.

## f) Quantidade de elementos:
Lê números até "fim" e exibe cada valor único com sua quantidade de repetições, na ordem de primeira aparição. Usa uma lista auxiliar `ja_exibidos` para controlar o que já foi mostrado e `.count()` para contar ocorrências — evitando imprimir a mesma mensagem várias vezes para valores repetidos.

## g) k-ésimo maior valor:
Dada uma lista de inteiros e um k, exibe o k-ésimo valor.

## h) Multiplique por k:
Recebe uma lista em uma única linha e um valor k, e imprime todos os elementos multiplicados por k na mesma linha. Trabalha o detalhe crítico de **espaço final na saída** (`print(..., end=" ")`), exigido por muitos juízes online.

## i) Listinha de compras:
Lê itens até "fim" (case-insensitive) e exibe tudo em ordem alfabética crescente. Exercita `sort(key=str.lower)` para ordenação **case-insensitive** — sem isso, maiúsculas viriam antes de minúsculas por causa da tabela ASCII.

## j) Palavras que começam com vogal:
Lê palavras até "fim" e exibe apenas as que começam com vogal (maiúscula ou minúscula). Trabalha acesso ao primeiro caractere (`palavra[0]`), normalização com `.lower()` e checagem de pertencimento em string (`in "aeiou"`).
