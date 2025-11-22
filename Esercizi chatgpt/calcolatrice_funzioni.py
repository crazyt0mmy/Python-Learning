def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def num_check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

run = True 
Operatori = ('+', '-', '*', '/')

while run:
    n1 = input("Inserire il primo numero: ")
    n2 = input("Inserire il secondo numero: ")
    opp = input("Operazione (+, -, *, /, q): ")
    if opp in Operatori and num_check(n1) and num_check(n2):
        if opp == '+':
            print(add(float(n1), float(n2)))
        if opp == '-':
            print(sub(float(n1), float(n2)))
        if opp == '*':
            print(mul(float(n1), float(n2)))
        if opp == '/':
            print(div(float(n1), float(n2)))            
    elif opp == 'q':
        run = False
    else:
        print("Operatore non valido")
        
