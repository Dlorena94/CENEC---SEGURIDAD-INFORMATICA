class Alumno:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del alumno:")
        self.materia=input("Ingrese la materia:")
        self.nota=float(input("Ingrese la nota:"))
        
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Materia:", self.materia)
        print("Nota:", self.nota)
        
    def calificacion(self):
        if self.nota>=5:
            print("Aprobado")
        else:
            print("Suspenso")
            
alumno1=Alumno()
alumno1.imprimir()
alumno1.calificacion()

alumno2=Alumno()
alumno2.imprimir()
alumno2.calificacion()