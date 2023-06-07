# https://neps.academy/br/exercise/1486
N = int(input())
digitos = []

for _ in range(N):
    digito = int(input())
    if digito == 0:
        del digitos[-1]
    else:
        digitos.append(digito)

# digitos = [int(input()) for _ in range(N)]

# new_digito = []
# for index, digito in enumerate(digitos):
#     if digito == 0:
#         del digitos[index - 1]

print(sum(digitos))
