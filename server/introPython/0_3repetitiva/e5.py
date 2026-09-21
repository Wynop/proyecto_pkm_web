total = 0
count = 0

while total < 50:
    total += float(input("Introduce el valor del artículo: "))
    count += 1

print(f"Se han comprado {count} artículos y el total ascienda a {total:.2f}€")
