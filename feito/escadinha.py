# https://neps.academy/br/exercise/165

"""
podemos percorrer a sequência de números e verificar as diferenças entre números consecutivos. 
Se a diferença entre dois números não for igual à diferença entre os números anteriores, então temos uma nova escadinha.
"""


def escadinha(N: int, sequência: list[int]):
    if N <= 2:
        return 1  # Qualquer sequência com 1 ou 2 números é uma escadinha

    diferença_atual = sequência[1] - sequência[0]
    quantidade_de_escadinhas_encontradas = 1

    for valor in range(2, N):
        if sequência[valor] - sequência[valor - 1] != diferença_atual:
            diferença_atual = sequência[valor] - sequência[valor - 1]
            quantidade_de_escadinhas_encontradas += 1

    return quantidade_de_escadinhas_encontradas


if __name__ == "__main__":
    N = int(input())
    sequencia = list(map(int, input().split()))

    resultado = escadinha(N, sequencia)

    print(resultado)
