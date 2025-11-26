def mayormenor(lista):
    """Encuentra e imprime el valor mayor y menor de una lista."""
    
    if not lista:
        print("La lista está vacía.")
        return

    may = lista[0]
    men = lista[0]
    
    
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
        elif lista[x] < men: 
            men = lista[x]
            
    print("El valor mayor de la lista es", may)
    print("El valor menor de la lista es", men)


lista = []
cantidad = 5 

for x in range(cantidad):
    valor = int(input(f"Ingrese valor {x+1}: "))
    lista.append(valor)

print("\n--- RESULTADOS MAYOR Y MENOR ---")
mayormenor(lista) 

suma_total = sum(lista)
cantidad_total = len(lista) 

print("\n--- CÁLCULO DE LA MEDIA ---")

if cantidad_total > 0:
    media = suma_total / cantidad_total
    
    print(f"La lista de valores es: {lista}")
    print(f"La suma total es: {suma_total}")
    print(f"La cantidad de valores es: {cantidad_total}")
    print(f"La media (promedio) es: {media:.2f}") 
else:
    print("La lista está vacía. No se puede calcular la media.")