p = 23  # Número primo
g = 5   # Generador

# Claves privadas elegidas por Alicia y Benito
a = 6  # Clave privada de Alicia
b = 15  # Clave privada de Benito

# Cálculo de las claves públicas
# Alicia envía A a Benito
A = (g ** a) % p
print(f"Clave pública de Alicia (A): {A}")

# Benito envía B a Alicia
B = (g ** b) % p
print(f"Clave pública de Benito (B): {B}")

# Cálculo de la clave compartida
# Alicia calcula la clave compartida S usando la clave pública de Benito
S_Alicia = (B ** a) % p
print(f"Clave compartida calculada por Alicia (S_Alicia): {S_Alicia}")

# Benito calcula la clave compartida S usando la clave pública de Alicia
S_Benito = (A ** b) % p
print(f"Clave compartida calculada por Benito (S_Benito): {S_Benito}")

# Verificación de que ambas claves compartidas son iguales
if S_Alicia == S_Benito:
    print(f"Éxito, la clave compartida es: {S_Alicia}")
else:
    print("Error, las claves compartidas no coinciden.")

