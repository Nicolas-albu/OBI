import random


def gerar_entradas_maximas():
    # Número máximo de salões de convivência
    S = random.randint(2, 1000)

    # Número máximo de túneis
    T = random.randint(1, S * (S - 1) // 2)

    # Definir os túneis
    tuneis = set()
    while len(tuneis) < T:
        x = random.randint(1, S)
        y = random.randint(1, S)
        if x != y:
            tuneis.add((x, y))

    # Número máximo de sugestões de passeio
    P = random.randint(1, 1000)

    # Sugestões de passeio
    passeios = []
    for _ in range(P):
        n = random.randint(1, S)  # Número de salões no passeio
        sequencia = random.sample(range(1, S + 1), n)
        passeios.append([n] + sequencia)

    # Salvar as entradas geradas em um arquivo de texto
    with open("saida.txt", "w") as file:
        file.write(f"{S} {T}\n")
        for tunel in tuneis:
            file.write(f"{tunel[0]} {tunel[1]}\n")
        file.write(f"{P}\n")
        for passeio in passeios:
            file.write(" ".join(map(str, passeio)) + "\n")


# Gerar as entradas máximas e salvar no arquivo "saida.txt"
gerar_entradas_maximas()
