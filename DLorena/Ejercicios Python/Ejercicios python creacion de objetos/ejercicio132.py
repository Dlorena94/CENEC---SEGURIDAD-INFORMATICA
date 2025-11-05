def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li

def imprimir_mayor20(li):
    print("Elementos de la lista mayores a 20")
    
    for x in range(len(li)):
        if li[x]>20:
            print(li[x])
            
lista=carga_lista()
imprimir_mayor20(lista)