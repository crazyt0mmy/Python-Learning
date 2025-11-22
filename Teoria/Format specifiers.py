# format specifiers = {value:flags} formatta un valora in base alla flag impostata

prezzo1 = 3.14235
prezzo2 = -987.65
prezzo3 = 1200.12

print(f"Prezzo1: €{prezzo1:.2f}") # Mostro solo due numeri dopo la virgola mettendo .(numeri dopo la virgola)f
print(f"Prezzo2: €{prezzo2:10}")  # Il numero ha 10 spazi per essere visualizzato
print(f"Prezzo2: €{prezzo2:010}") # Gli spazzi vuoti vengono riempiti da 0
print(f"Prezzo2: €{prezzo2:<10}") # I numeri vengono spostati a sinistra sempre con 10 spazi a disposizione
print(f"Prezzo2: €{prezzo2:^10}") # I numeri vengono spostati al centro sempre con 10 spazi a disposizione
print(f"Prezzo3: €{prezzo3: }")   # Serve a mostrare il segno del numero solo se negativo
print(f"Prezzo3: €{prezzo3:+}")   # Serve a mostrare il segno del numero 
print(f"Prezzo3: €{prezzo3:,}")   # Divide il numero ogni tre