import random

min = 1 
max = 100
x = random.randint(min, max)
errori = 0
Attivo = True

print(f"Indovina un numero casuale tra {min} e {max}")

while Attivo:
    ris = input("Inserisce la risposta: ")

    if ris.isdigit():
        ris = int(ris)
        errori += 1
        if ris == x:
            errori -= 1
            print("Hai indovinato!")
            print(f"Hai sbagliato {errori} volte prima di indovinare")
            Attivo = False
        elif ris < min or ris > max:    
            print(f"Inserire un numero tra {min} e {max}")   
            errori -= 1
        elif ris < x:
            print("Valore troppo basso, riprova")
        else:
            print("Valore troppo alto, riprova")
    else:
        print(f"{ris} non è un valore valido")
        print(f"Inserire un numero tra {min} e {max}")
