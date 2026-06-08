def mine_block(self, transactions: list[dict]) -> Block:
    previous = self.last_block
    block = Block(
        index=previous.index + 1,
        previous_hash=previous.hash,
        timestamp=time.time(),
        transactions=transactions,
    )
    prefix = "0" * self.difficulty
    while not block.hash.startswith(prefix):
        block.nonce += 1
        block.hash = block.calculate_hash()
    self.chain.append(block)
    return block
