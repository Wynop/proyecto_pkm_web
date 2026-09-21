NOMBRES = ["bolsa", "lapiz", "lechuga", "alfombra"]

BUSQUEDA = input("Busqueda: ")
isin = False

for e in NOMBRES:
    if e == BUSQUEDA:
        isin = True
        break

if isin:
    print(f"Encontrado: «{BUSQUEDA}»")
else:
    print(f"No hay ningún producto llamado «{BUSQUEDA}»")
