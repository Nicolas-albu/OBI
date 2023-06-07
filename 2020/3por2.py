# https://neps.academy/br/exercise/975
N = int(input())

precos = sorted([int(input()) for _ in range(N)], reverse=True)

# grupos = []
# resultado: int = 0

# Minha 1 ° solução
# for index in range(N):
#     if index % 3 == 0:
#         grupos.append(precos[index : index + 3])

#         if len(grupos[-1]) > 2:
#             grupos[-1].pop()
#         resultado += sum(grupos[-1])

# Solução do ChatGPT
# for index in range(N):
#     if index % 3 != 2:
#         resultado += precos[index]

# Minha 2° solução
resultado = sum(precos[index] for index in range(N) if index % 3 != 2)

print(resultado)
