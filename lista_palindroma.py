# https://neps.academy/br/exercise/1725

N = int(input()) - 1
lista = list(map(int, input().split()))

ponteiro_inicio, ponteiro_final = 0, 0
quantidade_contracoes: int = 0

for index in range(N - 1):
    index_final = N - index
    ponteiro_inicio, ponteiro_final = lista[index], lista[index_final]

    if ponteiro_inicio > ponteiro_final:
        proximo_valor_ponteiro_final = lista[index_final - 1]
        quantidade_contracoes += 1

    elif ponteiro_inicio < ponteiro_final:
        proximo_valor_ponteiro_inicio = lista[index + 1]
        quantidade_contracoes += 1

print(quantidade_contracoes)
