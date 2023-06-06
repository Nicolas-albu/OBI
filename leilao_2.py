N = int(input())

nome_ganhador: str = ""
maior_lance: int = 0

for _ in range(N):
    nome, valor_lance = [input() for _ in range(2)]
    valor_lance = int(valor_lance)

    if valor_lance > maior_lance:
        maior_lance = valor_lance
        nome_ganhador = nome

print(nome_ganhador)
print(maior_lance)
