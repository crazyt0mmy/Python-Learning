num_pad = ((1, 2, 3),(4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for lista in num_pad:
    for elementi in lista:
        print(elementi, end=" ")
    print()

