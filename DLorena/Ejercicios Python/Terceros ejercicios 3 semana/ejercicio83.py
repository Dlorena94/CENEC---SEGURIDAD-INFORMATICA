lista=[]
for x in range(5):
    valor=int(input("Ingrese el valor:"))
    lista.append(valor)
    
mayor=lista[0]
for x in range (1,5):
    if lista[x]>mayor:
        mayor=lista[x]
print("Lista completa:")
print(lista)
print("El mayor de la lista es:")
print(mayor)

cantidad=0
for x in range(5):
    if lista[x]==mayor:
        cantidad=cantidad+1
if cantidad>1:
    print("El mayor que se repite en la lista es:", mayor)
    