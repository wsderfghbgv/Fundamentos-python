expresiones = [
    "5 + 3 * 2",
    "8 / 2 + 4 * 3",
    "(7 + 3) * 2 - 5",
    "10 - 4 + 2 * 3",
    "(10 / 2) * (3 + 2) - 4",
    "2 + 3 * (4 - 1)",
    "5 * 2 ** 3",
    "6 + 4 / 2 ** 2",
    "10 % 3 + 2 * 5",
    "(8 + 2) * 3 ** 2",
    "7 + 2 * (3 + 5) / 4",
    "2 ** 3 * 4 / 2",
    "9 - 6 + 3 ** 2",
    "(7 - 2) * 5 + 3 ** 2",
    "4 * 2 ** 3 / 8 + 1",
]

for indice, expresion in enumerate(expresiones, start=1):
    print(f"Ejercicio {indice}: {expresion} = {eval(expresion)}")
