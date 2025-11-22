investimento = 0
interesse = 0
tempo = 0

while investimento <= 0:
    investimento = float(input("Quanto si vuole investire: "))
    if investimento <= 0:
        print("L'investimento deve essere positivo")

while interesse <= 0:
    interesse = float(input("Quant'è l'interesse: "))
    if interesse <= 0:
        print("L'interesse deve essere positivo")

while tempo <= 0:
    tempo = int(input("Tempo: "))
    if tempo <= 0:
        print("Il tempo deve essere positivo")

ris = investimento * pow((1 + interesse / 100), tempo)
print(f"Conto dopo {tempo} anni: €{ris:.2f}")




