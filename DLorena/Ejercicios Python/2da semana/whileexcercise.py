x=1
suma=0
while x<=3:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    x=x+1
promedio=suma/3
print("La suma de los valores es:")
print(suma)
print("El promedio es:")
print(promedio)

aprobado1=0
suspenso2=0

while x<=10:
    nota=int(input("Ingrese nota:"))
    if nota>=5:
        aprobado1=aprobado1+1
    else:
        suspenso2=suspenso2+1
    x=x+1
print("Cantidad de los alumnos aprobados con 5 o iguales a 5")
print(aprobado1)
print("Cantidad de alumnos reprobados nota inferior a 5")
print(suspenso2)

x=1 
x=0
aprobado1=0
suspenso2=0

while x<=10:
    nota=int(input(f"Ingrese nota {x}:"))
    if nota>=5:
        aprobado1=aprobado1+1
    else:
        suspenso2=suspenso2+1
    x=x+1
print(f"Cantidad de los alumnos aprobados {aprobado1}")
print(f"Cantidad de alumnos reprobados {suspenso2}")

