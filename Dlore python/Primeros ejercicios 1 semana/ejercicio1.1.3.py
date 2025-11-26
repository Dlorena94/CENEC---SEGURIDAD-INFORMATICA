base_imponible=float(input("Ingrese la base imponible por unidad (€):"))
unidades=int(input("Ingrese la cantidad de las unidades: "))

importe_bruto=base_imponible * unidades

descuento=importe_bruto * 0.10 
subtotal=importe_bruto - descuento

Iva=subtotal * 0.21
total_final=subtotal+Iva

print("\n--- Detalle del calculo ---")
print("Importe bruto: €", round(importe_bruto, 2))
print("Descuento (10%): €", round(descuento, 2))
print("Subtotal (con descuento): €", round(subtotal, 2))
print("Iva (21%): €", round (Iva, 2))
print("Total final (con Iva): €", round(total_final, 2))

