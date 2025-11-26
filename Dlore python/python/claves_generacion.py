# 1. Generación de claves

# Alicia genera su par de claves
key_alicia = DSA.generate(2048)

# Benito genera su par de claves
key_benito = DSA.generate(2048)

# 2. Alicia firma un mensaje

# Definimos el mensaje que Alicia quiere enviar
mensaje = b"Hola Benito, este mensaje esta firmado por Alicia."

# Alicia genera el hash del mensaje
hash_mensaje = SHA256.new(mensaje)

# Alicia firma el hash del mensaje usando su clave privada
firmante = DSS.new(key_alicia, 'fips-186-3')
firma = firmante.sign(hash_mensaje)

print("Mensaje enviado por Alicia: ", mensaje)
print("Firma generada por Alicia: ", firma.hex())

# 3. Benito verifica la firma

# Benito recibe el mensaje y la firma
mensaje_recibido = mensaje  # En la vida real, este mensaje sería recibido por la red
firma_recibida = firma  # En la vida real, la firma sería recibida por la red

# Generamos el hash del mensaje recibido por Benito
hash_recibido = SHA256.new(mensaje_recibido)

# Benito verifica la firma usando la clave pública de Alicia
verificador = DSS.new(key_alicia.publickey(), 'fips-186-3')

try:
    verificador.verify(hash_recibido, firma_recibida)
    print("La firma es válida. El mensaje es auténtico y fue enviado por Alicia.")
except ValueError:
    print("La firma no es válida. El mensaje puede haber sido modificado o no proviene de Alicia.")

# 4. Benito responde a Alicia firmando un mensaje

mensaje_benito = b"Hola Alicia, confirmo que he recibido tu mensaje."

# Benito firma su mensaje
hash_mensaje_benito = SHA256.new(mensaje_benito)
firmante_benito = DSS.new(key_benito, 'fips-186-3')
firma_benito = firmante_benito.sign(hash_mensaje_benito)

print("Mensaje enviado por Benito: ", mensaje_benito)
print("Firma generada por Benito: ", firma_benito.hex())

# 5. Alicia verifica la firma de Benito

# Alicia recibe el mensaje de Benito y su firma
mensaje_recibido_benito = mensaje_benito
firma_recibida_benito = firma_benito

# Alicia verifica la firma de Benito usando la clave pública de Benito
hash_recibido_benito = SHA256.new(mensaje_recibido_benito)
verificador_benito = DSS.new(key_benito.publickey(), 'fips-186-3')

try:
    verificador_benito.verify(hash_recibido_benito, firma_recibida_benito)
    print("La firma de Benito es válida. El mensaje es auténtico y fue enviado por Benito.")
except ValueError:
    print("La firma de Benito no es válida. El mensaje puede haber sido modificado o no proviene de Benito.")
