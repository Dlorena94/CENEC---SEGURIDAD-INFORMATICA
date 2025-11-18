# Paso 1: Cálculo de la clave pública de Alicia
p = 23  # Número primo
q = 11  # Otro primo
h = 2
g = pow(h, (p - 1) // q, p)
x = 10  # Clave privada de Alicia
y = pow(g, x, p)  # Clave pública de Alicia
print("Clave pública de Alicia (y):", y)

# Paso 2: Generación de la firma digital
# Hash del mensaje
H = 5  # Hash simulado del mensaje "Hola"
k = 3  # Número aleatorio
r = pow(g, k, p) % q
print("Valor de r:", r)

# Usamos el algoritmo extendido de Euclides para calcular el inverso de k mod q
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception("No tiene inverso")
    else:
        return x % m

k_inv = mod_inverse(k, q)

s = (k_inv * (H + x * r)) % q
print(f"Valores de la firma digital: r = {r}, s = {s}")

# Paso 3: Verificación de la firma por parte de Benito
def verify_signature(H, r, s):
    if not (0 < r < q and 0 < s < q):
        return False
    w = mod_inverse(s, q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r

# Verificamos la firma
if verify_signature(H, r, s):
    print("La firma es válida.")
else:
    print("La firma no es válida.")
