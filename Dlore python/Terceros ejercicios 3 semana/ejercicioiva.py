def iva (importe):
    total_iva=importe*0.21
    total_factura=importe+total_iva
    print(f"Importe es {importe} el iva es {total_iva} el total es: {total_factura}")

def pedir_datos():
    dato=float(input("Indica el importe:"))
    iva(dato)
    
pedir_datos()


