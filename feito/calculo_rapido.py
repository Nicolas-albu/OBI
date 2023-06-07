# https://neps.academy/br/exercise/1724
S, A, B = [int(input()) for _ in range(3)]

sum_digits = lambda number: sum(int(digit) for digit in number)

numbers: list[int] = [
    number for number in range(A, B + 1) if sum_digits(str(number)) == S
]

print(len(numbers))
