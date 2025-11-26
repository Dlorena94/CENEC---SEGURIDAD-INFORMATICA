class producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = float(precio)  # antes: precioint (error)

    def imprimir_producto(self):
        print(f"El producto es {self.nombre} y su precio es {self.precio:.2f} €")


class fabricante:
    def __init__(self, nombre_fabri, pais):
        self.nombre_fabri = nombre_fabri  # antes guardabas en self.nombre
        self.pais = pais

    def imprimir_fabricante(self):
        print(f"El fabricante es {self.nombre_fabri} y su país es {self.pais}")


class movil(producto, fabricante):
    def __init__(self, id, nombre, precio, nombre_fabri, pais, ram, almacenamiento):
        # Llamadas explícitas a los constructores de los padres
        producto.__init__(self, id, nombre, precio)
        fabricante.__init__(self, nombre_fabri, pais)
        self.ram = ram
        self.almacenamiento = almacenamiento

    def imprimirTicket(self):
        print(f"Su móvil es {self.nombre}, su precio es {self.precio:.2f} €, "
              f"del fabricante {self.nombre_fabri}")

    def datos_tecnicos(self):
        print(f"El móvil {self.nombre} tiene {self.ram} de RAM y {self.almacenamiento} de almacenamiento")


# --- Pruebas (¡ojo a los paréntesis!) ---
movil1 = movil(1, "Honor", 500, "Huawei", "China", "32 Gigas", "256 gigas")
movil2 = movil(2, "Samsung Galaxy", 900, "Samsung", "Corea", "64 Gigas", "512 gigas")

movil1.imprimirTicket()
movil1.datos_tecnicos()

movil2.imprimirTicket()
movil2.datos_tecnicos()
