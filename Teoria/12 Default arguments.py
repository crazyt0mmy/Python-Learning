# Argomenti di default = un valore predefinito per alcuni parametri
#                        Il valore predefinito viene usato quando l’argomento viene omesso
#                        Rendono la tua funzione più flessibile e riducono il numero di argomenti necessari
#                        Ordine degli argomenti: 
#                        1. Posizionali, 2. DEFAULT, 3. Keyword, 4. Arbitrari

# def netto(listino, sconto = 0, irpef = 0.10):           # eccoli siii
#     return listino * (1 - sconto) * (1 + irpef)
# print(netto(500, 0.1, 0))

import time

def count(fine, inizio = 0):
    for x in range(inizio, fine+1):
        print(x)
        time.sleep(1)
    print("Fatto!")

count(10)