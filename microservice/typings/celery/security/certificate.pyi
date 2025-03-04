"""
This type stub file was generated by pyright.
"""

"""X.509 certificates."""
class Certificate:
    """X.509 certificate."""
    def __init__(self, cert) -> None:
        ...
    
    def has_expired(self):
        """Check if the certificate has expired."""
        ...
    
    def get_pubkey(self):
        """Get public key from certificate."""
        ...
    
    def get_serial_number(self):
        """Return the serial number in the certificate."""
        ...
    
    def get_issuer(self):
        """Return issuer (CA) as a string."""
        ...
    
    def get_id(self):
        """Serial number/issuer pair uniquely identifies a certificate."""
        ...
    
    def verify(self, data, signature, digest):
        """Verify signature for string containing data."""
        ...
    


class CertStore:
    """Base class for certificate stores."""
    def __init__(self) -> None:
        ...
    
    def itercerts(self):
        """Return certificate iterator."""
        ...
    
    def __getitem__(self, id):
        """Get certificate by id."""
        ...
    
    def add_cert(self, cert):
        ...
    


class FSCertStore(CertStore):
    """File system certificate store."""
    def __init__(self, path) -> None:
        ...
    


