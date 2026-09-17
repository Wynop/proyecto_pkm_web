year = int(input("año: "))

if year <= 0:
    print("Error")
elif(year % 400 == 0):
    print("Es bisiesto")
else:
    if(year % 100 == 0):
        print("No es bisiesto")
    elif(year % 4 == 0):
       print("Es bisiesto")
    else:
        print("No es bisiesto")
