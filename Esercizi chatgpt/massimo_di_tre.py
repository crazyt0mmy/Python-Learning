def massimo(a, b, c):
    return max(a, b ,c)

def num_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

n1 = input("Inserire il primo numero: ")
n2 = input("Inserire il secondo numero: ")
n3 = input("Inserire il terzo numero: ")

if num_check(n1) and num_check(n2) and num_check(n3):
    print(f"Il numero più grande è: {massimo(float(n1), float(n2), float(n3))}")
