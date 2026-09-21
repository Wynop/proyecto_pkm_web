PRECIOS = [89.95, 15.5, 199.0, 12.0, 24.9]
count = 0

for e in PRECIOS:
    if e >= 20:
        count += 1

print(f"De {len(PRECIOS)} hay {count} precios por encima de 20" )