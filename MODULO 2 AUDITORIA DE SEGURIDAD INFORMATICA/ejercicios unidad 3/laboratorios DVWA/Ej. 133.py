def cargar_lista():
    lis=[]
    for x in range(1, 4):
    valor=int(input("Ingrese el valor:"))
    lis.append(valor)
    return lis

def retornar_mayormenor(lis):
    ma=lis[0]
    me=lis[0]
    for x in range(len(lis)):
        if lis[x]>ma:
            ma=lis[x]
        else:
            if lis[x]<me:
                me=lis[x]
    return [ma,me]

# bloque principal del programa
lista=cargar_lista()
rango=retornar_mayormenor(lista)
print("Mayor elemento de la lista:")
print("Menor elemento de la lista:")
