frase = input("Inserire una stringa: ")

vocali = 0

for i in frase:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vocali += 1

print(f"Ci sono {vocali} vocali nella stringa")