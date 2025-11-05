def cargar_sueldos():
    sueldos=[]
    for x in range(5):
        su=int(input("Ingrese sueldo:"))
        sueldos.append(su)
    return sueldos


def imprimir_sueldos(sueldos):
    print("Listado de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])


def sueldos_mayor1200(sueldos):
    cant=0
    for x in range(len(sueldos)):
        if sueldos[x]>1200:
            cant=cant+1
    print("Cantidad de empleados con un sueldo superior a 4000:",cant)


def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma=suma+sueldos[x]
    promedio=suma//5
    return promedio

def sueldos_bajos(sueldos):
    pro=promedio(sueldos)
    print("Sueldo promedio de la empresa:",pro)
    print("Sueldos inferiores al promedio")
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print(sueldos[x])

sueldos=cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayor1200(sueldos)
sueldos_bajos(sueldos)