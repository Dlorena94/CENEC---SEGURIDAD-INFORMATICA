nombres=[]
for x in range(5):
    nom=input("Ingrese el nombre de la persona: ")
    nombres.append(nom)

nombre_menor=nombres[0]
for x in range(1,5):
    if nombres[x]<nombre_menor:
        nombre_menor=nombres[x]
        
print("Lista completa de nombres")
print(nombres)
print("Nombre menor en orden alfabetico")
print(nombre_menor)