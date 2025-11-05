class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
    
    def imprimir_producto(self):
        print(f"--- Detalles del Producto ---")
        print(f"ID del producto:{self.id_producto}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio:{self.precio:.2f} €")
        
      
class Fabricante(Producto): 
    
    def __init__(self, id_producto, nombre, precio, nombre_fabricante, pais):
        Producto.__init__(self, id_producto, nombre, precio) 
        
        self.nombre_fabricante = nombre_fabricante
        self.pais = pais
    
    def imprimir_fabricante(self):
        print(f"Fabricante: {self.nombre_fabricante}")
        print(f"País de Origen: {self.pais}")
        

class Celular(Fabricante):
    
    def __init__(self, id_producto, nombre, precio, ram, almacenamiento, nombre_fabricante, pais):
        Fabricante.__init__(self, id_producto, nombre, precio, nombre_fabricante, pais)
        
        self.ram = ram
        self.almacenamiento = almacenamiento
        
    def imprimir_ticket(self):
        print("\n--- TICKET DE COMPRA ---")
        self.imprimir_producto()
        self.imprimir_fabricante()
        print(f"Especificaciones: {self.ram} GB RAM / {self.almacenamiento} GB Almacenamiento")
        print("------------------------")
        

celular1 = Celular(
    id_producto="M001",
    nombre="Xiaomi 14",
    precio=999.50,
    ram=12,
    almacenamiento=256,
    nombre_fabricante="Xiaomi",
    pais="China"
) 

fabricante1= Fabricante(
    id_producto="F999",
    nombre="Info_Fabricante",
    precio=0.00,
    nombre_fabricante="Apple Inc.",
    pais="EE. UU."
)


celular1.imprimir_ticket()
fabricante1.imprimir_fabricante()
fabricante1.imprimir_producto()
