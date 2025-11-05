lista=[]
for x in range (5):
    valor=int(input("Ingrese el valor: "))
    lista.append(valor)
mayor=lista[0] 
for list in lista:
    if list>mayor:
        mayor=list
print("Lista completa")
print(lista)
print("Mayor de la lista")
print(mayor)
