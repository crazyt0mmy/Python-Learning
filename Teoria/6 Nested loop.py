# nested loop = Un loop dentro un altro loop (esterno, interno)

righe = int(input("Quante righe vuoi: "))
colonne = int(input("Quante colonne vuoi: "))
segno = input("Cosa vuoi mostrare: ")

for i in range(righe):
    for j in range(colonne):
        print(segno, end=" ")
    print()                    #uso end="" se voglio qualcosa dopo la riga senza andare a capo