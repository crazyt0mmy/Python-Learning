# *args = permette di passare più argomenti non-chiave
# **kwargs = permette di passare più argomenti parola-chiave
#            * operatore di spacchettamento
#            1. posizionale 2. default 3. parola-chiave 4. ARBITRARIO
from fontTools.misc.psOperators import ps_string


def add(*args):     #posso anche cambiare il nome di args
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Nicolò", "Andrea", "Rui", "III")

print(" ")


def print_address(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}: {values}")

print_address(street="Sesso 123",
              city="Detroit",
              state="MI",
              zip="1243")


def shipping_label(*args, **kwargs):        #devo avere prima args e dopo kwargs
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Nicolò", "Andrea", "Rui", "III",
               street="Sesso 123",
               pobox="PO box #1243",
               city="Detroit",
               state="MI",
               zip="1243"
               )