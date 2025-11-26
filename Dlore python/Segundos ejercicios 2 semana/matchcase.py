
opcion = 2

match opcion:
    case 1: 
        print("Has elegido la opcion 1")
    
    case 2:
        print("Has elegido la opcion 2")
        
    case 3:
        print("Has elegido la opcion 3")
    
    case _:
        print("Opcion no valida ")
        
print("Dias de la semana")
print("Escribe un numero del 1 al 7: ")

dia = input("Numero: ")

match dia:
    case "1":
        print("Hoy es Lunes.")
    case "2":
        print("Hoy es Martes.")
    case "3":
        print("Hoy es Miercoles.")
    case "4":
        print("Hoy es jueves.")
    case "5":
        print("Hoy es Viernes.")
    case "6":
        print("Hoy es Sabado.")
    case "7":
        print("Hoy es Domingo.")
        
        