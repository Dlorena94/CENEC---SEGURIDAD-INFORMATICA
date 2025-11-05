def producto(lista):
    prod=1
    for x in range(len(lista)):
        prod=prod*lista[x]
    return prod


lista=[1, 2, 3, 4, 5]
print("Lista:", lista)
print("Multiplicacion de todos sus elementos:",producto(lista))

cantidad_total= len(lista)
print("\n --- calculo de  la media --- ")

if cantidad_total>0:
    suma_total=sum(lista)
    
    media= suma_total/cantidad_total

print(f"La media (promedio) es: {media:.2f}")