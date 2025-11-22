# Collezioni = singole variabili che contengono più valori
# List = [] ordinata e sostotuibile
# Set = {} disordinata e immutabile, si possono aggiungere e rimuovere
# Tuple = () ordinata e immutabile

# frutti = ["mela", "pera", "banana", "pesca"]
# frutti = {"mela", "pera", "banana", "pesca"} se stampo questa lista l'ordine non sarà lo stesso
# frutti = ("mela", "pera", "banana", "pesca")

# print(len(frutti))                Con len capisco quante cose ci sono nella lista
# print("mela" in frutti)           Se c'è mela nella lista restituisce True altrimenti False
# frutti.append("anguria")          Uso append per aggiungere alla lista
# frutti.remove("mela")             Uso remove per togliere un elemento dalla lista
# frutti.insert(0, "melone")        Mette l'elemento nella posizione decisa
# frutti.sort()                     Mette la lista in ordine alfabetico
# frutti.reverse()                  Mette la lista al contrario
# frutti.clear()                    Svuota la lista
# print(frutti.index("pera"))       Restituisce la posizione di un elemento della lista
# print(frutti.count("banana"))     Conta quante volte compare una parola nella lista

# print(frutti)                   #Per accedere a un elemento uso []

# for i in frutti:
#     print(i)