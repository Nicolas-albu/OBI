N: int = int(input())
divisoes: list[int] = list(map(int, input().split()))
# divisoes = map(int, input().split())

divisoes = [divisao - 1 for divisao in divisoes]
# divisoes = map(lambda divisao: divisao - 1, divisoes)

print(sum(divisoes))
