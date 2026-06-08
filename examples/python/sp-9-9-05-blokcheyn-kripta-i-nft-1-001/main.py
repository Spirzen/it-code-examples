
import hashlib
import json

from time import time

class Block:
    def __init__(self, index, previous_hash, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time()
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        payload = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "nonce": self.nonce,
        }, sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()

def is_chain_valid(chain):
    """Та же идея, что в интерактиве: связь хешей и целостность каждого блока."""
    for i in range(1, len(chain)):
        if chain[i].previous_hash != chain[i - 1].hash:
            return False
        if chain[i].calculate_hash() != chain[i].hash:
            return False
    return True
