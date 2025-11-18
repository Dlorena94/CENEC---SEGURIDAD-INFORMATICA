import random
from sympy import mod_inverse

# Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para generar un número primo aleatorio en un rango
def generar_primo(rango_min, rango_max):
    primo = random.randint(rango_min, rango_max)
    while not es_primo(primo):
        primo = random.randint(rango_min, rango_max)
    return primo

# Paso 1: Generar dos primos pequeños p y q
p = generar_primo(50, 100)
q = generar_primo(50, 100)
print(f"Primos generados: p = {p}, q = {q}")

# Paso 2: Calcular n y phi(n)
n = p * q
phi_n = (p - 1) * (q - 1)
print(f"n = {n}, phi(n) = {phi_n}")

# Paso 3: Elegir e (el exponente público) tal que 1 < e < phi(n) y coprimo con phi(n)
e = 65537  # En RSA, 65537 es una elección común para e
print(f"e elegido: {e}")

# Paso 4: Calcular d (exponente privado), usando la inversa modular de e mod phi(n)
d = mod_inverse(e, phi_n)
print(f"Clave pública (e, n) = ({e}, {n})")
print(f"Clave privada (d, n) = ({d}, {n})")

# Paso 5: Cifrar un mensaje (convertimos "Hola" a un número)
mensaje_original = 72  # "Hola" simplificado como 72
print(f"Mensaje original: {mensaje_original}")

# Cifrado: C = M^e mod n
C = pow(mensaje_original, e, n)
print(f"Mensaje cifrado: {C}")

# Paso 6: Descifrar el mensaje
mensaje_descifrado = pow(C, d, n)
print(f"Mensaje descifrado: {mensaje_descifrado}")
