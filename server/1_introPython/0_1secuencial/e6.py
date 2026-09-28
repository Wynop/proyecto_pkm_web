name = input("Nombre del cliente: ")
uds = int(input("Unidades: "))
precio = float(input("Precio unidad(€): "))
iva = precio * 0.21 * uds

print()
print(f"FACTURA - {name}")
print(f"Base: {(uds * precio):.2f}")
print(f"IVA (21%): {iva:.2f}")
print(f"Total: {(iva + (uds * precio)):.2f}")