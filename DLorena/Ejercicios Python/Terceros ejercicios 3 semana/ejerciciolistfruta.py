frutas= ["manzana", "pera", "banano", "papaya"]
fruta=str.lower(input("Dime la fruta:"))

for fruit in frutas:
    if fruta == fruit:
        print(f"Fruta encontrada: {fruit}")
        break
else:
    print("La fruta no esta en la lista.")    
    