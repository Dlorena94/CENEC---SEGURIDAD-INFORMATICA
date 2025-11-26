def sumarizar(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

def mayor (lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may

def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men

def media(lista):
    suma_total=0
    cantidad=len(lista)
    
    if cantidad == 0:
        return 0

    for x in range(cantidad):
        suma_total += lista[x]
    media=suma_total/cantidad
    return media
    

lista_valores=[10, 56, 23, 120, 94]
resultado= media(lista_valores)
print("La lista completa es:")
print(lista_valores)
print("La suma de todos sus elemnetos es:", sumarizar(lista_valores))
print("El mayor valor de la lista es:", mayor(lista_valores))
print("El menor valor de la lista es:", menor(lista_valores))
print(f"La media de {lista_valores} es: {resultado}")
