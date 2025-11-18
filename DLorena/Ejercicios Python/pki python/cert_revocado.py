from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    NoEncryption
)
from datetime import datetime, timedelta
import os # Importamos os para verificar la existencia de archivos

# --- Función Principal ---
def create_ca_and_crl():
    # 1. Generar una clave privada para la CA
    print("1. Generando clave privada de la CA...")
    ca_private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # 2. Crear un certificado autofirmado para la CA
    print("2. Creando certificado autofirmado para la CA...")
    
    # Nombre de la CA (Subject y Issuer son iguales para un certificado autofirmado)
    ca_name = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"ES"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Cáceres"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Valencia de Alcántara"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Valentino"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"Valencia CA"),
    ])

    ca_certificate = x509.CertificateBuilder().subject_name(
        ca_name
    ).issuer_name(
        ca_name
    ).public_key(
        ca_private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        datetime.utcnow() + timedelta(days=365) # Válido por 1 año
    ).add_extension(
        x509.BasicConstraints(ca=True, path_length=None), critical=True,
    ).sign(
        ca_private_key, algorithm=hashes.SHA256(),
    )

    # 3. Guardar el certificado y la clave privada
    print("3. Guardando 'ca_certificate.pem' y 'ca_private_key.pem'...")

    with open("ca_certificate.pem", "wb") as f:
        f.write(ca_certificate.public_bytes(Encoding.PEM))

    with open("ca_private_key.pem", "wb") as f:
        f.write(ca_private_key.private_bytes(
            Encoding.PEM,
            PrivateFormat.PKCS8,
            NoEncryption()
        ))
    
    print("Archivos de la CA guardados correctamente.")

    # 4. Crear una CRL
    print("4. Creando Lista de Revocación de Certificados (CRL)...")
    
    # Inicializar el constructor de la CRL
    builder = x509.CertificateRevocationListBuilder().issuer_name(
        ca_certificate.subject # El emisor de la CRL es la CA
    ).last_update(
        datetime.utcnow() # Última actualización: ahora
    ).next_update(
        datetime.utcnow() + timedelta(days=7) # Próxima actualización: en 7 días
    )

    # Revocar un certificado (simulación)
    print("   -> Simulando la revocación de un certificado...")
    revoked_cert = x509.RevokedCertificateBuilder().serial_number(
        123456789 # Número de serie del certificado revocado
    ).revocation_date(
        datetime.utcnow() # Fecha de revocación: ahora
    ).build()
    
    # Añadir el certificado revocado a la CRL
    builder = builder.add_revoked_certificate(revoked_cert)

    # 5. Firmar la CRL con la clave privada de la CA
    crl = builder.sign(
        private_key=ca_private_key, 
        algorithm=hashes.SHA256()
    )

    # 6. Guardar la CRL
    print("5. Guardando 'crl.pem'...")
    with open("crl.pem", "wb") as f:
        f.write(crl.public_bytes(Encoding.PEM))
    
    print("\nCertificado CA y CRL generados correctamente.")
    print("-" * 50)


    # 7. Leer y analizar la CRL generada
    print("6. Leyendo y analizando la CRL generada...")
    # Verificar que el archivo existe antes de intentar leerlo
    if not os.path.exists("crl.pem"):
        print("Error: 'crl.pem' no se encontró para su análisis.")
        return

    with open("crl.pem", "rb") as f:
        crl_data = f.read()
    
    # Cargar la CRL desde el formato PEM
    loaded_crl = x509.load_pem_x509_crl(crl_data)

    # Imprimir detalles de la CRL
    print("\nDetalles de la CRL:")
    print(f"Emisor: {loaded_crl.issuer}")
    print(f"Última actualización: {loaded_crl.last_update_utc}")
    print(f"Próxima actualización: {loaded_crl.next_update_utc}")
    
    print("\nCertificados revocados:")
    # Iterar sobre los certificados revocados (debería haber 1)
    for revoked in loaded_crl:
        print(f"- Número de serie: {revoked.serial_number}, Fecha de revocación: {revoked.revocation_date}")

# Ejecutar la función principal
if __name__ == "__main__":
    create_ca_and_crl()