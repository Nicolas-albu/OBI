def pega_lances(N: int) -> list[tuple[str, int]]:
    lances: list[tuple] = []
    for _ in range(N):
        nome, valor_lance = [input() for _ in range(2)]
        lances.append((nome, int(valor_lance)))
    return lances


def encontra_maior_lance(lances: list[tuple]) -> tuple[str, int]:
    index_maior_valor_lance: int = 0
    for index, lance in enumerate(lances):
        if lance[1] > lances[index_maior_valor_lance][1]:
            index_maior_valor_lance = index
    return lances[index_maior_valor_lance]


if __name__ == "__main__":
    N = int(input())
    lances = pega_lances(N)
    maior_lance = encontra_maior_lance(lances)
    print(maior_lance[0])
    print(maior_lance[1])
