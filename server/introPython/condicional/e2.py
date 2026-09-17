uds = int(input("Unidades: "))

if(uds == 0):
    print("Agotado")
elif(uds <= 5):
    print("Últimas unidades")
else:
    print("Disponible")