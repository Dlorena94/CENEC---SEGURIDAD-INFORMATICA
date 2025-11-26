def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro
lado=int(input("Lado del cuadrado:"))
print("El perimetro es:",retornar_perimetro(lado))