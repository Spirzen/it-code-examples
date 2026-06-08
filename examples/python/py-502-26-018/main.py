class DataStore(ABC):
    @property
    @abstractmethod
    def capacity(self) -> int:
        pass
    
    @abstractmethod
    def store(self, key: str, value: bytes) -> None:
        pass
    
    @abstractmethod
    def retrieve(self, key: str) -> bytes:
        pass

class MemoryStore(DataStore):
    def __init__(self):
        self._data = {}
        self._max_size = 1024 * 1024  # 1 MB
    
    @property
    def capacity(self) -> int:
        return self._max_size
    
    def store(self, key: str, value: bytes) -> None:
        if len(value) > self.capacity:
            raise ValueError("Данные превышают ёмкость хранилища")
        self._data[key] = value
    
    def retrieve(self, key: str) -> bytes:
        return self._data[key]
