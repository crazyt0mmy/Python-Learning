import random

opzioni = ("sasso", "carta", "forbice")
running = True

while running:
    ris = None
    computer = random.choice(opzioni)
    while ris not in opzioni: 
        ris = input("Inserire una scelta (sasso, carta, forbice): ")

    print(f"Player: {ris}")
    print(f"Comptuter: {computer}")

    if ris == computer:
        print("Pareggio")
    elif ris == "carta" and computer == "sasso":
        print("Hai vinto")
    elif ris == "sasso" and computer == "forbice":
        print("Hai vinto")
    elif ris == "forbice" and computer == "carta":
        print("Hai vinto")
    else:
        print("Hai perso")

    again = input("Vuoi giocare di nuovo(y/n): ")
    if again != "y":
        running = False

print("Grazie per aver giocato!")