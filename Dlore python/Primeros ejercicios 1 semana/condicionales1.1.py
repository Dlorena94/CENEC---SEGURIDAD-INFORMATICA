nota=int(input("Ingrese su Nota:"))

if nota>=90:
    print("Sobresaliente")
elif nota>=80:
    print("Notable")
elif nota>=70:
    print("Aprobado")
else:
    print("Reprobado,Suspenso")
    
edad=int(input("Ingrese su Edad: "))
ingresos=float(input("Ingrese sus Ingresos: ")) 

if edad>18 and ingresos> 3000:
    print("Eres elegible para el crédito") 
else:
    print("No cumples los Requisitos")
    
    
    
es_admin = True

if es_admin:
    print("Tienes acceso como administrador.")
else:
    print("Acceso denegado.")

num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segunda valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)
        

num=int(input("Ingrese un valor:"))
if num==0:
    print("Se ingresó el cero")
else:
    if num>0:
        print("Se ingresó un valor positivo")
    else:
        print("Se ingresó un valor negativo")
        
        
num=int(input("Ingrese un valor de hasta tres dígitos positivo:"))
if num<10:
    print("Tiene un dígito")
else:
    if num<100:
        print("Tiene dos dígitos")
    else:
        if num<1000:
            print("Tiene tres dígitos")
        else:
            print("Error en la entrada de datos.")


totalpreguntas=int(input("Ingrese la cantidad total de preguntas del examen:"))
totalcorrectas=int(input("Ingrese la cantidad total de preguntas contestadas correctamente:"))
porcentaje=totalcorrectas * 100 / totalpreguntas
if porcentaje>=90:
    print("Nivel máximo")
else:
    if porcentaje>=75:
        print("Nivel medio")
    else:
        if porcentaje>=50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")
