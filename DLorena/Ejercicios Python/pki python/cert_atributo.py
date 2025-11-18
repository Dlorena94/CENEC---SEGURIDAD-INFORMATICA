# attribute_certificate_model.py

from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta
import uuid

# --- 1. Definición Conceptual de las Clases ---
# En un sistema real, no defines las clases tú mismo.
# Usarías las clases predefinidas de la librería,
# pero esto ayuda a entender la estructura.

class AttributeCertificateInfo:
    """Simula la estructura AttributeCertificateInfo."""
    def __init__(self, version, holder_name, issuer_name, serial):
        self.version = version
        self.holder = holder_name
        self.issuer = issuer_name
        self.serialNumber = serial
        self.attrCertValidityPeriod = None # Lo estableceremos después
        self.attributes = []
        self.issuerUniqueID = None # Opcional
        self.extensions = [] # Opcional

    def add_attribute(self, oid_str, value):
        """Agrega un atributo, por ejemplo, un rol."""
        # En la vida real, los atributos son complejos y se representan como X.509 Extensions o Attributes
        self.attributes.append({
            "oid": oid_str,
            "value": value
        })

    def set_validity(self, not_before, not_after):
        self.attrCertValidityPeriod = {
            "not_before": not_before,
            "not_after": not_after
        }

    def __str__(self):
        return f"""
        --- AttributeCertificateInfo ---
        Versión: {self.version}
        Titular (Holder): {self.holder}
        Emisor (Issuer): {self.issuer}
        No. Serie: {self.serialNumber}
        Validez: {self.attrCertValidityPeriod['not_before'].strftime('%Y-%m-%d')} a {self.attrCertValidityPeriod['not_after'].strftime('%Y-%m-%d')}
        Atributos: {self.attributes}
        """

class AttributeCertificate:
    """Simula el AttributeCertificate ::= SIGNED { AttributeCertificateInfo }."""
    def __init__(self, info_obj):
        self.info = info_obj
        self.signature_algorithm = "SHA256withRSA" # Algoritmo de firma
        self.signature_value = "SIMULATED_SIGNATURE_DATA" # El resultado de la firma

    def __str__(self):
        return f"AttributeCertificate (Firmado con {self.signature_algorithm})\n{str(self.info)}"

# --- 2. Creación del Objeto ---

# 1. Definir los nombres para el Titular y el Emisor
holder_cn = "Usuario Autorizado"
issuer_cn = "Autoridad de Atributos del Departamento de TI"

# 2. Crear la información base
info = AttributeCertificateInfo(
    version=2, # v2 es el estándar
    holder_name=holder_cn,
    issuer_name=issuer_cn,
    serial=int(uuid.uuid4().int % (10**20)) # Número de serie grande simulado
)

# 3. Establecer el periodo de validez
now = datetime.utcnow()
info.set_validity(
    not_before=now,
    not_after=now + timedelta(days=365)
)

# 4. Agregar atributos (El Rol es un atributo clave en estos certificados)
# Usando OID (Object Identifier) simulado
info.add_attribute(
    oid_str="1.3.6.1.4.1.311.20.2", # OID común para "Role"
    value="Administrador de Sistemas"
)

# 5. Finalmente, crear el certificado completo con la firma (simulada)
attr_cert = AttributeCertificate(info)


# --- 3. Ejecución y Visualización en VS Code ---
print("--- Modelo Conceptual del Certificado de Atributo ---")
print(attr_cert)

# Para un caso de uso real, usarías 'cryptography' para leer o generar certificados X.509
print("\n--- Nota: Uso de Librería 'cryptography' para Certificados Reales ---")

# Ejemplo de cómo se vería una representación de Nombre del Sujeto real
subject_name_real = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "ES"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Mi Empresa"),
    x509.NameAttribute(NameOID.COMMON_NAME, holder_cn),
])

print(f"Representación real del nombre del titular (X.509): {subject_name_real}")