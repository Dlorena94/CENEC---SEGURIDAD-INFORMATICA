import hashlib
import binascii

# Mensaje original
mensaje = "Hola, mundo"

# Convertir el mensaje a bytes
mensaje_bytes = mensaje.encode()

# Mostrar el mensaje en bytes
print("Mensaje en bytes:")
print(mensaje_bytes)

# Fase 1: Preparación del mensaje (padding)
def padding(mensaje_bytes):
    mensaje_bin = ''.join(format(byte, '08b') for byte in mensaje_bytes)
    mensaje_len = len(mensaje_bin)

    # Agregar '1' al final del mensaje
    mensaje_bin += '1'

    # Rellenar con ceros hasta que el largo sea congruente con 448 mod 512
    while len(mensaje_bin) % 512 != 448:
        mensaje_bin += '0'

    # Agregar la longitud original del mensaje al final, en 64 bits
    mensaje_bin += format(mensaje_len, '064b')

    return mensaje_bin

mensaje_padded = padding(mensaje_bytes)

# Mostrar el mensaje después del padding
print("\nMensaje después del padding:")
print(mensaje_padded)

# Fase 2: Hash utilizando hashlib para obtener el hash final (con todas las rondas internas)
hash_sha256 = hashlib.sha256(mensaje_bytes)

# Debido a la complejidad del algoritmo SHA-256, algunas de las etapas no se pueden implementar
# sin una reescritura detallada del algoritmo. Estas etapas incluyen la expansión del mensaje
# y las rondas de compresión, que involucran operaciones matemáticas avanzadas (rotaciones, mezclas bit a bit, etc.).

# Obtener el valor del hash en formato hexadecimal
hash_hex = hash_sha256.hexdigest()

# Mostrar el resultado del hash
print("\nHash SHA-256 final (resultado):")
print(hash_hex)





