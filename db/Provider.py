
from models import models
from abc import ABC, abstractmethod
from typing import Dict, List, TypeVar, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from .Document import TDocument
from .Collection import TCollection


class Provider(ABC):
    _collections: Dict[str, List['TDocument']]

    def __init__(self):
        self._models = models
        self._collections = dict({})

    @property
    def models(self):
        return self._models

    def getCollection(self, name: str):
        return self._collections.get(name)

    def findItem(self, collectionName: str, itemId: str) -> Optional['TDocument']:
        coll: 'TCollection' = self._collections.get(collectionName)
        if (coll):
            return coll.findById(itemId)
        return None

    def createItem(self, collectionName: str, item) -> Optional['TDocument']:
        coll: 'TCollection' = self._collections.get(collectionName)
        if (coll):
            return coll.create(item)
        return None

    def deleteItem(self, collectionName: str, itemId: str) -> Optional['TDocument']:
        coll: 'TCollection' = self._collections.get(collectionName)
        if (coll):
            return coll.deleteById(itemId)
        return None

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def save(self): pass


TProvider = TypeVar('TProvider', bound=Provider)
