# while = esegue del codice MENTRE una condizione è vera

x = int(input("Metto un numero tra 1 -10: "))

while x < 1 or x > 10:
    print(f"{x} non è valido")
    x = int(input("Metto un numero tra 1 -10: "))

print(f"Hai scelto il numero {x}")