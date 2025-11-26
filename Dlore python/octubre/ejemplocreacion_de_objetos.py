class Persona:
    
    def inicializar(self,nombre,apellidos,cp,provincia):
        self.nombre=nombre
        self.apellidos=apellidos
        self.cp=cp
        self.provincia=provincia
    
    def imprimir(self):
        print("Nombre", self.nombre,"Apellidos", self.apellidos, "cp",self.cp, "Provincia", self.provincia)
        

persona1=Persona()
persona1.inicializar("Pedro", "Perez Pepito", "29590", "Malaga")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla", "Campano Cazas", "29001", "Almeria")
persona2.imprimir()

persona3=Persona()
persona3.inicializar("Lorena","Ros Porr", "29006","Cadiz" )
persona3.imprimir()
