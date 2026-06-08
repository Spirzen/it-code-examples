def payload_dict(self) -> dict[str, Any]:
    return {
        "type": "transfer",
        "sender": self.sender,
        "recipient": self.recipient,
        "asset": self.asset,
        "amount": self.amount,
        "nonce": self.nonce,
    }

def sign(self, keys: KeyPair) -> None:
    message = canonical_json(self.payload_dict()).encode("utf-8")
    sig = keys.sign(message)
    self.signature_b64 = base64.b64encode(sig).decode("ascii")
