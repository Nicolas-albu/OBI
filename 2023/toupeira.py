# from time import time

# initial = time()

S, T = map(int, input().split())

grafo: dict = {}

for _ in range(T):
    X, Y = map(int, input().split())

    if X not in grafo:
        grafo[X] = [Y]
    else:
        grafo[X].append(Y)

    if Y not in grafo:
        grafo[Y] = [X]
    else:
        grafo[Y].append(X)

P = int(input())


def verifica_sequencia(total: int, sequencia: list[int], grafo_sequencia: dict) -> bool:
    for index in range(total - 1):
        if sequencia[index + 1] not in grafo_sequencia[sequencia[index]]:
            return False

    return True


sequencias: list[tuple] = []

for _ in range(P):
    N, *C = map(int, input().split())

    sequencias.append((N, tuple(C)))

quantidades_possiveis: int = 0
for _, sequencia in enumerate(sequencias):
    if verifica_sequencia(*sequencia, grafo):
        quantidades_possiveis += 1

# final = time()

print(quantidades_possiveis)
# print(f"tempo total de {final - initial}s")
