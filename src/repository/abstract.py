import abc
from pathlib import Path 

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, reference_id: str) -> Path:
        raise NotImplementedError