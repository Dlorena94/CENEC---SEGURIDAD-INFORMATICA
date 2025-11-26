class Felino:
    
    def inicializar(self,nombre,comida):
        self.nombre=nombre
        self.comida=comida
       
            
    def come(self):
        print("Mi Gato", self.nombre,"Come", self.comida)
    
    def maulla(self):
        print("Mi Gato", self.nombre, "Maulla") 

felino1=Felino()
felino1.inicializar("Ivan", "Atun")
felino1.come()
felino1.maulla()



