
capitales = {
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma",
    "Reino Unido": "Londres",
}

# 2) Acceso por clave
print("Capital de España:", capitales["España"])

# 3) Comprobar existencia y mostrar
pais = "Alemania"
if pais in capitales:
    print(f"Capital de {pais}:", capitales[pais])
else:
    print(f"{pais} no está en el diccionario")
