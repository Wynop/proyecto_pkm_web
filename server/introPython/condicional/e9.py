SALDO = 60.0
PRECIO = 24.5
CANTIDAD = 2
STOCK = 5

if STOCK < 0:
    print("Producto agotado")
elif CANTIDAD > STOCK:
    print("Saldo insuficiente")
elif SALDO < PRECIO * CANTIDAD:
    print("Saldo insuficiente")
else:
    print("Compra realizada")
