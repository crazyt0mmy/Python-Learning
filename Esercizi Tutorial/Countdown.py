import time

tempo = int(input("Inserire il tempo in secondi: "))

for i in reversed(range(tempo)):
    secondi = i % 60
    minuti = int(i / 60) % 60
    ore = int(i / 3600)
    print(f"{ore:02}:{minuti:02}:{secondi:02}")
    time.sleep(1)

print("SESSO ADESSO SISISISI")