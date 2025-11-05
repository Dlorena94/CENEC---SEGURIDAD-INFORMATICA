nombres=["Albert", "Ana", "Paco"]
print(nombres[1])

meses=["Abril", "Junio", "Julio", "Diciembre"]
print(meses[0])
print(meses[3])

indica_meses="Diciembre"

for month in meses:
    if indica_meses==month:
        print("Mes encontrado") 
    else:
        print(f"No encontrado {month}")
        
for month in meses:
    if indica_meses==month:
        print(f"Mes encontrado: {month}") 
        break
    
else:
    print("El mes no esta en la lista")
    
ciudades=["Cali", "Malaga", "Santader", "Barranquilla"]
ciudad=input("Que ciudad estas buscando: ")

for city in ciudades:
    if ciudad == city:
        print(f"Ciudad encontrada: {city}")
        break
else: 
    print("La ciudad no esta en la lista")
    
