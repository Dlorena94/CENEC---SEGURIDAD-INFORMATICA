import hashlib  # Importamos la librería para usar funciones hash

# 1. Función para obtener el hash de un mensaje usando SHA-256
def calculate_sha256_hash(message):
    # Crear un objeto sha256
    sha256 = hashlib.sha256()
    # Convertir el mensaje a bytes y actualizar el objeto sha256
    sha256.update(message.encode('utf-8'))
    # Devolver el hash en formato hexadecimal
    return sha256.hexdigest()

# 2. Demostración con un mensaje
message = "Hola, este es un ejemplo de hash con SHA-256."
hash_result = calculate_sha256_hash(message)

# 3. Mostramos el resultado
print("Mensaje original:", message)
print("Hash con SHA-256:", hash_result)

# 4. Probamos la sensibilidad a pequeños cambios (modificamos una letra)
message_modified = "Hola, este es un ejemplo de has con SHA-256."  # Cambiamos una letra
hash_result_modified = calculate_sha256_hash(message_modified)

print("\nMensaje modificado:", message_modified)
print("Hash con SHA-256 (modificado):", hash_result_modified)

# Comprobamos que los hashes son completamente diferentes aunque solo se cambió una letra
