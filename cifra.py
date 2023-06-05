alphabet: list[str] = "a b c d e f g h i j k l m n o p q r s t u v x z".split()
vowels: list[str] = "a e i o u".split()

entrada = input().strip()

cifra: str = ""

index_vowels = [index for index, _ in enumerate(alphabet) if index in vowels]

for index, letter in enumerate(entrada):
    cifra += letter
