M, N = map(int, input().split())

# matriz: list[list] = []

# for _ in range(M):
#     linha: list = [map(int, input().split())]

#     matriz.append(linha)

matriz: list[list] = [[*map(int, input().split())] for _ in range(M)]
quantidade_vendida: int = 0

P = int(input())

for _ in range(P):
    I, J = map(int, input().split())
    I, J = I - 1, J - 1
    # I -= 1
    # J -= 1

    if matriz[I][J] != 0:
        matriz[I][J] -= 1
        quantidade_vendida += 1

print(quantidade_vendida)
