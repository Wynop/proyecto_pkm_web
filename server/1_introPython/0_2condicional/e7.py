print("(0)->Ver catálogo,\n(1)->Bucar un producto\n(2)->Ver el carrito")
BUSQUEDA = input("Seleccione una opción: ")

if BUSQUEDA == "0": print("Catálogo")
elif BUSQUEDA == "1": print("Producto")
elif BUSQUEDA == "2": print("Carrito")
else: print("Opción no valida")