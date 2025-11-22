# indexing = accedere ad un elementi di una sequenza con []
#            [inizio : fine : step]


carta = "1234-5678-9012-3456"
# Voglio il primo carattere della string
# print(carta[0])

# Voglio i primi quattro caratteri della string
# print(carta[0 : 4])

# Voglio i caratteri fino alla fine della string da una determinata posizione
# print(carta[5:])

# Se uso i numeri negativi parto al contrario
# print(carta[-2])

# Se non metto niente su inizio e fine ma volgio uno step devo mettere ::
# In questo caso stampo ogni secondo carattere
# print(carta[::2])

#### Programma per trovare i quattro numeri finali ####

#num_finale = carta[-4:]
#print(f"XXXX-XXXX-XXXX-{num_finale}")

#### Programma per invertire il numero della carta ####

# Utilizzo lo step -1 per partire dalla fine

carta = carta[::-1]
print(carta)