def is_pari(n):
    if n%2==0:
        return True
    else:
        return False
    
def num_check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

n = input("Inserire un numero: ")

if num_check(n):
    if is_pari(int(n)):
        print("Numero pari")
    else:
        print("Numero dispari")
