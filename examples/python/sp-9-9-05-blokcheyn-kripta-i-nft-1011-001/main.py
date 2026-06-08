@dataclass
class Blockchain:
    chain: list[Block] = field(default_factory=list)
    difficulty: int = 2

    def is_valid(self) -> tuple[bool, str]:
        prefix = "0" * self.difficulty
        for i, block in enumerate(self.chain):
            if block.hash != block.calculate_hash():
                return False, f"блок {i}: хеш не совпадает с содержимым"
            if i > 0 and block.previous_hash != self.chain[i - 1].hash:
                return False, f"блок {i}: разорвана ссылка на предыдущий"
            if i > 0 and not block.hash.startswith(prefix):
                return False, f"блок {i}: не выполнен учебный PoW"
        return True, "ok"
