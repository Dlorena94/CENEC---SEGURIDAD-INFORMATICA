base_imponible=float(input("Ingrese la base imponible por unidad (€):"))
unidades=int(input("Ingrese la cantidad de las unidades: "))
importe_bruto=base_imponible * unidades
descuento=importe_bruto * 0.10 
importe_final=importe_bruto - descuento
print("Importe bruto: €", round(importe_bruto, 2))
print("Descuento (10%): €", round(descuento, 2))
print("Importe final con descuento: €", round(importe_final, 2))
