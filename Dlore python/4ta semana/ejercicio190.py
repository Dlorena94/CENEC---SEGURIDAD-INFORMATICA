class Empleado:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")
        self.apellidos=input("Ingrese los apellidos:")
        self.sueldo=float(input("Ingrese el sueldo:"))
        
        
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Apellidos:",self.apellidos)
        print("Sueldo:",self.sueldo)
        
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")
    
    def porcentaje(self):
        impuesto= self.sueldo * 0.21
        print(f"El 21% de impuestos a pagar es: {impuesto:.2f}")
        print(f"Sueldo que te queda {self.sueldo - impuesto:.2f}")
        

            
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()  
empleado1.porcentaje()
