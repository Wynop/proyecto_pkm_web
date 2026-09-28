PRECIOS = [89.95, 15.5, 199.0, 12.0, 24.9]
caro = 0
total = 0
media = 0

for e in PRECIOS:
    total += e
    if e > caro:
        caro = e
media = total / len(PRECIOS)

print(f"El más caro vale {caro}, el total és {total:.2f} y la media {media:.2f}")