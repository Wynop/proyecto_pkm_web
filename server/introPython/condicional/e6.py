BUSQUEDA = input("Busqueda: ")
Resultado = input("Resultado: ")

if BUSQUEDA is None: print("No se envió el formulario de búsqueda")
elif bool(BUSQUEDA) == False: print("Se buscó sin escribir nada")
elif bool(BUSQUEDA) == True and Resultado is None: print(f"Sin resultados para «{BUSQUEDA}»")
elif bool(BUSQUEDA) == True and bool(Resultado) == True: print(f"Encontrado:\n «{Resultado}»")