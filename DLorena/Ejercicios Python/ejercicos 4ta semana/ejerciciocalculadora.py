class Calculadora:
    def __init__(self):
        self.num1=float(input("Ingrese el numero:"))
        self.num2=float(input("Ingrese el numero:"))
        
        self.suma = self.num1 + self.num2
        self.resta = self.num1 - self.num2
        self.multiplicacion = self.num1 * self.num2
        self.division = self.num1 / self.num2

    def imprimir(self):
        print("La suma es:",self.suma)
        print("La resta es:",self.resta)
        print("La multiplicacion es:",self.multiplicacion)
        print("La division es:", self.division)
        

            
calculadora1= Calculadora()
calculadora1.imprimir()

calculadora2=Calculadora()
calculadora2.imprimir()
