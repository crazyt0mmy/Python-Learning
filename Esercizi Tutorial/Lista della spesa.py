cibo = []
prezzo = []
totale = 0

while True:
    item = input("Inserire un cibo da comprare (q to quit): ")
    if item.lower() == "q":
        break
    else:
        cost = float(input(f"Quanto costa {item}: "))
        prezzo.append(cost)        
        cibo.append(item)

print("----CARRELLO----")

for i in cibo:
    print(i, end=" ")

for i in prezzo:
    totale += i

print()
print(f"Il tuo totale è: €{totale}")