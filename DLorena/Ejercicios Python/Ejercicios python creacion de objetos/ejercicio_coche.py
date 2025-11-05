class Coche:
    
    def inicializar(self,motor,ruedas,tipo):
        self.motor=motor
        self.ruedas=ruedas
        self.tipo=tipo
       
            
    def acelerar(self):
        print("El coche", self.tipo, "El motor", self.motor, " ", self.ruedas) 
          
    def frenar(self):
        print("El coche", self.tipo, "El motor", self.motor, " ", self.ruedas)    

coche1 = Coche()
coche1.inicializar("V6", 4, "Deportivo")
coche1.acelerar()

coche2 = Coche()
coche2.inicializar("V8", 4, "SUV")
coche2.frenar()

coche3 = Coche()
coche3.inicializar("Eléctrico", 4, "Compacto")
coche3.acelerar()
