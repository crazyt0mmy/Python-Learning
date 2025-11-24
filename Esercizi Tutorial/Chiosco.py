menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "patatine": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "coca": 3.00,
        "limonata": 4.25}

spesa = []
totale = 0

print("------MENU------")
for chiavi, valori in menu.items():
    print(f"{chiavi}: €{valori:.2f}")
print("----------------")

while True:
    ogg = input("Cosa vuoi prendere (q per uscire): ")
    if ogg.lower() == "q":
        break
    elif menu.get(ogg) != None:
        spesa.append(ogg)  
        totale += menu.get(ogg)
    else:
        print("Prodotto non disponibile")

print("----Spesa finale----")
for item in spesa:
    print(item, end=" ")

print()
print(f"Il totale della spesa è: €{totale:.2f}")



    
