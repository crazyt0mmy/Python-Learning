def num_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
x = input("Inserire il numero: ")

if num_check(x):
    for i in range(1,11):
        ris = float(x) * i
        print(ris)