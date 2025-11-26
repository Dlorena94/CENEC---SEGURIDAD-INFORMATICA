x=1
mayor=0
menor=0
n=int(input("Ingrese número de edades a contar: "))

while x<=n:
    edad=int(input("Ingrese su edad: "))
    if edad>=18:
        mayor=mayor+1
    else:
        menor=menor+1
    x=x+1
print("Mayores de edad: ")
print(mayor)
print("Manores de edad: ")
print(menor) 