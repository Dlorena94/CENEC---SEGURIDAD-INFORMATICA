class Carro:
    def inicializar(self,motor,ruedas,tipo):
        self.motor=motor
        self.ruedas=ruedas
        self.tipo=tipo
        
    def acelerar(self):
        print("El carro", self.tipo,"acelera")
        
    def frenar(self):
        print("El carro", self.tipo, "frena")
        
        
        
coche1=Carro()
coche1.inicializar("16v","4","rojo")
coche1.acelerar()
coche1.frenar()

coche2=Carro()
coche2.inicializar("v8","5","azul")
coche2.acelerar()
coche2.frenar()


coche3=Carro()
coche3.inicializar("","","")
coche3.acelerar()
coche3.frenar()