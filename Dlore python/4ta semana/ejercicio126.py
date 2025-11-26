def cantidad_vocal_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=='a' or palabra[x]=="A":
            cant=cant+1
    return cant
palabra=input("Ingrese una palabra:")
print("La palabra", palabra, "tiene", cantidad_vocal_a(palabra), "a")