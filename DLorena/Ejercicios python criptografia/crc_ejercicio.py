# Ejemplo completo de CRC (Cyclic Redundancy Check)
# ============================================

# 1. Convertir mensaje en bits (simulación)
def string_to_bits(message):
    return ''.join(format(ord(i), '08b') for i in message)


# 2. Función que realiza la división binaria (mod 2)
def xor_division(dividend, divisor):
    """Realiza una división XOR binaria y retorna el resto."""
    remainder = list(dividend[:len(divisor)])  # Copia inicial del dividendo
    divisor_length = len(divisor)

    # Realizamos la división paso a paso (XOR en cada paso)
    for i in range(len(dividend) - divisor_length + 1):
        if remainder[0] == '1':  # Solo si hay un 1, aplicamos XOR
            for j in range(divisor_length):
                remainder[j] = str(int(remainder[j]) ^ int(divisor[j]))

        remainder.pop(0)  # Eliminar el bit más a la izquierda
        if i + divisor_length < len(dividend):  # Añadir un nuevo bit del dividendo
            remainder.append(dividend[i + divisor_length])

    return ''.join(remainder)


# 3. Codificar un mensaje con CRC
def crc_encode(message, generator_polynomial):
    """Realiza la codificación CRC de un mensaje usando un polinomio generador."""
    message_bits = string_to_bits(message)

    # Añadir ceros al final del mensaje (de tamaño del generador - 1)
    padded_message = message_bits + '0' * (len(generator_polynomial) - 1)

    # Obtener el residuo
    remainder = xor_division(padded_message, generator_polynomial)

    # Mensaje codificado: concatenamos el mensaje original con el residuo CRC
    encoded_message = message_bits + remainder

    return encoded_message, remainder


# 4. Verificar si el mensaje tiene errores utilizando CRC
def crc_verify(received_message, generator_polynomial):
    """Verifica si un mensaje recibido tiene errores aplicando CRC."""
    remainder = xor_division(received_message, generator_polynomial)
    no_error = all(bit == '0' for bit in remainder)  # Si el residuo es cero, no hay error
    return no_error


# ============================================
# Ejemplo práctico de uso de CRC
# ============================================

message = "Hola"
generator_polynomial = "1101"  # Polinomio generador de ejemplo (CRC-3)

# Codificamos el mensaje
encoded_message, remainder = crc_encode(message, generator_polynomial)
print(f"Mensaje original: {message}")
print(f"Polinomio generador: {generator_polynomial}")
print(f"Mensaje codificado CRC: {encoded_message}")
print(f"Residuo (CRC): {remainder}")

# Simulación de recepción del mensaje (correcto)
received_message = encoded_message
is_valid = crc_verify(received_message, generator_polynomial)
print(f"\nMensaje recibido (sin errores): {received_message}")
print(f"¿Válido?: {is_valid}")

# Simulación de recepción del mensaje con error
# Introducimos un error: invertimos un bit
received_message_with_error = list(encoded_message)
received_message_with_error[3] = '1' if encoded_message[3] == '0' else '0'
received_message_with_error = ''.join(received_message_with_error)

is_valid_with_error = crc_verify(received_message_with_error, generator_polynomial)
print(f"\nMensaje recibido con error: {received_message_with_error}")
print(f"¿Válido?: {is_valid_with_error}")
