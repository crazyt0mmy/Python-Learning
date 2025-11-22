# Dizionario = una collezione di coppie di {key:value} ordinata e sostotuibile. No duplicati 

capitali = {"USA": "Washington",
            "India": "New Delhi",
            "Italy": "Rome"}

# print(capitali.get("USA"))

# if capitali.get("Italy"):
#     print("La capitale esiste")
# else:
#     print("La capitale non esiste")

# capitali.update({"Germany": "Berlin"})            Aggiungo un elemento al dizionario
# capitali.update({"USA": "Sesso"})                 Aggiorno USA con sesso senza crearne un altro
# capitali.pop("Italy")                             Tolgo un elemento
# capitali.popitem()                                Toglie l'ultimo elemento
# capitali.clear()                                  Pulisce la lista
# chiavi = capitali.keys()                          .keys restituisce le chiavi 
# valore = capitali.values()                        .values restituisce il valore delle chiavi
# capitali.items()                                  restituisce una cosasimile a una lista 2D

for chiavi, valore in capitali.items():
    print(f"{chiavi} -> {valore}")