class Seguro:
    def __init__(self):
        self.modelo=input("Ingrese el modelo:")
        self.kilometros=int(input("Ingrese los kilometros:"))
        self.añomatri=int(input("Ingrese año de matriculacion:"))
        
    def imprimir(self):
        print("Modelo:", self.modelo)
        print("Kilometros:", self.kilometros)
        print("Año de matriculacion:", self.añomatri)
    
    def pagar_seguro(self):
        if self.añomatri >= 2010:
            print("Pagas un 10% mas")
            
        else:
            print("Pagas un 5%")

carro1=Seguro()
carro1.imprimir()
carro1.pagar_seguro()
print("____________________________")

carro2=Seguro()
carro2.imprimir()
carro2.pagar_seguro()
print("____________________________")

carro3=Seguro()
carro3.imprimir()
carro3.pagar_seguro()

