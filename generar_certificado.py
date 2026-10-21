from datetime import datetime, timedelta, timezone
from pathlib import Path

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Carpeta donde Nginx buscará el certificado
carpeta = Path(
    r"D:\Benjamin_Gil\UVEG\Despliegue de aplicaciones web y móviles"
    r"\Retos\nginx-1.30.6\conf\ssl"
)

carpeta.mkdir(parents=True, exist_ok=True)

# Generar clave privada
clave = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Datos del certificado
nombre = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, "inventario.test")
])

ahora = datetime.now(timezone.utc)

certificado = (
    x509.CertificateBuilder()
    .subject_name(nombre)
    .issuer_name(nombre)
    .public_key(clave.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(ahora - timedelta(minutes=5))
    .not_valid_after(ahora + timedelta(days=365))
    .add_extension(
        x509.SubjectAlternativeName([
            x509.DNSName("inventario.test")
        ]),
        critical=False
    )
    .add_extension(
        x509.BasicConstraints(ca=False, path_length=None),
        critical=True
    )
    .sign(clave, hashes.SHA256())
)

# Guardar clave privada
(carpeta / "inventario.key").write_bytes(
    clave.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
)

# Guardar certificado público
(carpeta / "inventario.crt").write_bytes(
    certificado.public_bytes(serialization.Encoding.PEM)
)

print("Certificado SSL generado correctamente.")
print("Certificado:", carpeta / "inventario.crt")
print("Clave privada:", carpeta / "inventario.key")