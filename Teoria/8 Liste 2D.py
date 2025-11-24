# lista 2D è una lista composta da altre liste 

frutta = ["mela", "pera"]
verdura = ["cavolo", "ravanello"]
carne = ["pollo", "manzo"]

spesa = [frutta, verdura, carne]

print(spesa[1][1])                     # Per stampare una lista dentro uso [] e funzionano a righe [0] = frutta [1] = verdura ecc...
                                       # Per stampare un elemento di una lista devo fare [lista][elemento

for liste in spesa:                        # Stampo le tre listed
    for elementi in liste:                        # Stampo ogni singolo elemento delle liste
        print(elementi, end=", ")
    print()