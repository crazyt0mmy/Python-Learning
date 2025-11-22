frase = input("Inserire una frase: ")
frase = frase.lower()

if frase == frase[::-1]:
    print("La frase è palindroma")
else:
    print("La frase non è palindroma")