# V, *contas = map(int, [int(input()) for _ in range(4)])

# quantidade_contas_pagas: int = 0

# for conta in contas:
#     if V >= conta:
#         quantidade_contas_pagas += 1
#         V -= conta

# print(quantidade_contas_pagas)


def verifica_contas(V, contas: list[int]) -> int:
    """Implementação do algoritmo DC/recursão"""
    quantidade_contas = 0

    if len(contas) == 0:
        return 0

    if V >= contas[0]:
        V -= contas[0]
        quantidade_contas += 1

    return quantidade_contas + verifica_contas(V, contas[1:])


if __name__ == "__main__":
    V, *contas_pagar = map(int, [int(input()) for _ in range(4)])

    print(verifica_contas(V, contas_pagar))
