# https://neps.academy/br/exercise/824
N, M = list(map(int, input().split()))
I, R = list(map(int, input().split()))

infectados = {I}
encontrou_infectado = False

for numero_da_reuniao in range(1, M + 1):
    A, *reuniao = list(map(int, input().split()))
    # reuniao = {int(numero) for numero in input().split()[1:]}
    # reuniao = set(list(map(int, input().split()))[1:])

    if not encontrou_infectado and R == numero_da_reuniao:
        infectados |= set(reuniao)
        encontrou_infectado = True
    elif encontrou_infectado and set(reuniao) & infectados:
        infectados |= set(reuniao)

print(len(infectados))

# N -> total de amigos do grupo
# M -> total de dias em houve reunião
# I -> identificador do amigo que foi infectado
# R -> identificador da reunião que I participou infectado

# amigos identificados de 1 à N
# reunião identificados de 1 à M
