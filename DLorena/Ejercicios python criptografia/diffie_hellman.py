import random

# Paso 1: Selección de parámetros públicos (p y g)
p = 23  # Un número primo público
g = 5   # Un generador público (base)

print(f"Parámetros públicos:\n  p = {p}\n  g = {g}\n")

# Paso 2: Cada usuario selecciona su clave privada
# Usuario A elige su clave privada (secreto)
a = random.randint(1, p-1)
print(f"Usuario A selecciona su clave privada (secreto) a = {a}")

# Usuario B elige su clave privada (secreto)
b = random.randint(1, p-1)
print(f"Usuario B selecciona su clave privada (secreto) b = {b}")

# Paso 3: Cálculo de claves públicas
# Usuario A calcula su clave pública
A_pub = (g ** a) % p
print(f"Usuario A calcula su clave pública: A_pub = {A_pub}")

# Usuario B calcula su clave pública
B_pub = (g ** b) % p
print(f"Usuario B calcula su clave pública: B_pub = {B_pub}")

# Paso 4: Intercambio de claves públicas y cálculo de la clave compartida
# Usuario A recibe la clave pública de B y calcula la clave compartida
K_A = (B_pub ** a) % p
print(f"\nUsuario A calcula la clave compartida: K_A = {K_A}")

# Usuario B recibe la clave pública de A y calcula la clave compartida
K_B = (A_pub ** b) % p
print(f"Usuario B calcula la clave compartida: K_B = {K_B}")

# Verificamos que ambas claves compartidas son iguales
if K_A == K_B:
    print(f"\n¡El intercambio de claves ha sido exitoso! Clave compartida: {K_A}")
else:
    print("\nError en el intercambio de claves")
