N = int(input())
sequência = list(map(int, input().split()))

diferença_atual = sequência[1] - sequência[0]
quantidade_de_escadinhas_encontradas = 1

compara_diferenças = (
    lambda valor_atual, valor_anterior: valor_atual - valor_anterior == diferença_atual
)

for valor in range(2, N):
    if not compara_diferenças(sequência[valor], sequência[valor - 1]):
        diferença_atual = sequência[valor] - sequência[valor - 1]
        quantidade_de_escadinhas_encontradas += 1
