def invoice(username, amount, date):
    print(f"Hello {username}")
    print(f"Your bill of €{amount:.2f} is due: {date}")

# invoice("Vanella", 104.67, "01/01")

def nome(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

x = input("Inserire il proprio nome: ")
y = input("Inserire il proprio cognome: ")

full_name = nome(x, y)
print(full_name)

