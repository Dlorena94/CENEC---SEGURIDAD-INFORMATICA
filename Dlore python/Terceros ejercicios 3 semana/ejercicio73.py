lista=[8, 1, 9, 2, 10]
cantidad=0

for list in lista:
    if list>=7:
        cantidad=cantidad+1
print("Elementos de la lista con valores iguales o superiores a 7")
print(cantidad)


nombres=["juan", "ana", "marcos", "carlos", "luis"]
cantidad=0

for names in nombres:
    if len(names)>=5:
        cantidad=cantidad+1

print("Todos los nombres son: ")
print(nombres)
print("Cantidad de nombres con 5 o mas caracteres: ")
print(cantidad)