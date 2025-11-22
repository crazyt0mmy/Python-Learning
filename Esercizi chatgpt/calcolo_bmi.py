def num_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
peso = input("Peso: ")
altezza = input("Quanto sei alto: ")

if num_check(peso) and num_check(altezza):
    peso = float(peso)
    altezza = float(altezza)
    bmi = peso / (altezza * altezza)
    if bmi < 18.5:
        print("Sottopeso")
    elif bmi >= 18.5 and bmi < 25:
        print("Normopeso")
    elif bmi >= 25 and bmi < 30:
        print("Sovrappeso")
    elif bmi >= 30 and bmi < 35:    
        print("Obeso classe I")
    elif bmi >= 35 and bmi < 40:
        print("Obeso classe II")
    else:
        print("Obeso classe III")
