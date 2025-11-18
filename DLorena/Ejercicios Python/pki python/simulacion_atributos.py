# simulacion_certificados.py

# ==============================================================================
# 1. INSTALACIÓN DE LIBRERÍAS Y MÓDULOS
# ==============================================================================
# La instalación se realiza mediante el comando: pip install cryptography
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.x509.oid import NameOID
import cryptography.x509 as x509
from datetime import datetime, timedelta
# Importamos serialization de nuevo, por si acaso no estaba ya en el path (redundante pero seguro)
from cryptography.hazmat.primitives import serialization

# ==============================================================================
# 2. GENERACIÓN DE CLAVES Y CERTIFICADOS
# ==============================================================================

# Generación de claves privadas para CA y AA
def generar_clave_privada():
    """Genera una clave privada RSA."""
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

# Creación de un certificado digital (CA)
def crear_certificado_digital(clave_privada, nombre_emisor):
    """
    Crea un certificado digital (X.509) autofirmado (Self-Signed).
    Este representa al Certificado de la Autoridad Certificadora (CA).
    """
    # Define el Sujeto (subject) y el Emisor (issuer) como el mismo (autofirmado)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"ES"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Cáceres"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Valencia de Alcántara"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, nombre_emisor),
        x509.NameAttribute(NameOID.COMMON_NAME, u"CA de ejemplo"),
    ])

    certificado = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        clave_privada.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        datetime.utcnow() + timedelta(days=365) # Válido por 1 año
    ).add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True,
    ).sign(clave_privada, hashes.SHA256()) # Firma el certificado

    return certificado

# Creación de un Certificado de Atributo (AA)
def crear_certificado_atributo(clave_privada, certificado_digital, atributos):
    """
    Crea un certificado de atributo.
    - El Emisor (issuer) será la entidad representada por certificado_digital.subject.
    - Los atributos se insertan como una Extensión No Reconocida (UnrecognizedExtension).
    """
    # 1. Definición del Emisor (Issuer) del Certificado de Atributo
    # Se toma el Sujeto (subject) del certificado digital (la CA) como el emisor de los atributos
    issuer = certificado_digital.subject

    # 2. Definición del Sujeto (Subject - Titular) del Certificado de Atributo
    # En un certificado de atributo, el "subject" es el titular (holder) de los atributos.
    # Aquí se simula un nombre.
    subject = x509.Name([
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Titular de Atributos"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"Atributos de ejemplo"),
    ])

    # 3. Construcción del Certificado de Atributo (simulación con CertificateBuilder)
    # Nota: La librería 'cryptography' no tiene una clase directa 'AttributeCertificateBuilder',
    # por lo que a menudo se usa CertificateBuilder y se ajustan las extensiones.
    certificado_atributo = x509.CertificateBuilder().subject_name(
        subject # El Titular (Holder)
    ).issuer_name(
        issuer # El Emisor (AA)
    ).public_key(
        clave_privada.public_key() # Clave pública de la Autoridad de Atributos (AA)
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        datetime.utcnow() + timedelta(days=30) # Periodo de validez corto
    ).add_extension(
        # Inserción de los atributos reales como una Extensión No Reconocida
        # OID "1.2.3.4.5.6.7.8.1" es un OID de prueba/ejemplo.
        x509.UnrecognizedExtension(
            oid=x509.ObjectIdentifier("1.2.3.4.5.6.7.8.1"),
            value=atributos.encode(), # Codifica la cadena de atributos en bytes
            critical=False,
        ),
        critical=False,
    ).sign(clave_privada, hashes.SHA256()) # Firma con la clave privada de la AA

    return certificado_atributo

# ==============================================================================
# 3. EXPORTACIÓN Y EJEMPLO DE USO
# ==============================================================================

# Serialización de los certificados
def exportar_certificado(certificado, filename):
    """Serializa el certificado a formato PEM y lo guarda en un archivo."""
    # 'wb' es para escribir en modo binario
    with open(filename, "wb") as f:
        f.write(certificado.public_bytes(serialization.Encoding.PEM))

# --- Ejemplo de uso ---

# 1. Generación de claves para la CA y la AA
clave_ca = generar_clave_privada()
clave_aa = generar_clave_privada()

# 2. Creación del Certificado Digital (CA)
certificado_digital = crear_certificado_digital(clave_ca, "CA de Prueba")

# 3. Definición de atributos y creación del Certificado de Atributo (AA)
atributos = "Rol: Administrador; Permiso: Acceso Completo"
certificado_atributo = crear_certificado_atributo(clave_aa, certificado_digital, atributos)

# 4. Exportación de los certificados a archivos
exportar_certificado(certificado_digital, "certificado_digital.pem")
exportar_certificado(certificado_atributo, "certificado_atributo.pem")

# 5. Mostrar resultados en consola
print("--- SIMULACIÓN DE PKI (CA + AA) ---")
print("\nCertificado Digital (CA):")
# Al imprimir, se muestra una representación del objeto (no todo el contenido codificado)
print(certificado_digital) 

print("\nCertificado de Atributo (AA):")
print(certificado_atributo)

print("\n¡Exportación completada!")
print("Se han generado los archivos 'certificado_digital.pem' y 'certificado_atributo.pem' en la misma carpeta.")