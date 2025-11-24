# Keyword arguments = un argomento preceduto da un identificatore
#                     Aiuta la leggibilità del codice
#                     L’ordine degli argomenti non importa
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# hello("Ciao", title="Mr.", last="Vanella", first="Teo")

# for x in range(1, 11):
#     print(x, end=" ")

def phone(paese, area, primo, ultimo):
    return f"{paese} {area} {primo} {ultimo}"

numero = phone(paese=1, area=123, primo=456, ultimo=7890)

print(numero)