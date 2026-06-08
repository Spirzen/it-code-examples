from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def sign_transaction(private_key, transaction_data: str) -> bytes:
    return private_key.sign(
        transaction_data.encode(),
        ec.ECDSA(hashes.SHA256()),
    )

def verify_signature(public_key, transaction_data: str, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            transaction_data.encode(),
            ec.ECDSA(hashes.SHA256()),
        )
        return True
    except Exception:
        return False

private_key = ec.generate_private_key(ec.SECP256K1())
public_key = private_key.public_key()
tx = '{"to":"0xBob","amount":1}'
sig = sign_transaction(private_key, tx)
assert verify_signature(public_key, tx, sig)
