valor_envio = float(input("valor envio: "))

if(valor_envio >= 50):
    print(f"Envío gratis \nTotal: {valor_envio}€")
elif(valor_envio >= 20):
    print(f"Coste envío 3.95€ \nTotal: {valor_envio + 3.95}€")
else:
    print(f"Coste envío 5.95€ \nTotal: {valor_envio + 5.95}€")
