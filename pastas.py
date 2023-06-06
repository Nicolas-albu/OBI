P, N = list(map(int, input().split()))

posicoes_pastas = sorted([int(input()) for _ in range(N)])

resultado = ""
for pos in posicoes_pastas:
    if posicoes_pastas.count(pos) > P:
        resultado = "N"
        break
    resultado = "S"

print(resultado)
# if N % 2 != 0:
#     P -= 1

# resultado = N % P

# print("S" if resultado in (0, 1) else "N")
