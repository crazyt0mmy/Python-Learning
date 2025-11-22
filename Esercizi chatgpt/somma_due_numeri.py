def somma(a,b):
    return a+b

def num_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

n1 = input("Inserire il primo numero: ")
n2 = input("Inserire il secondo numero: ")

if num_check(n1) and num_check(n2):
    print(somma(float(n1),float(n2)))
else:
    print("Bisogna inserire due numeri")

