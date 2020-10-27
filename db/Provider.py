from .Collection import Collection, ResultT
from models import models
from abc import ABC, abstractmethod


class Provider(ABC):
    def __init__(self):
        self._models = models
        self._collections = dict({})

    @property
    def models(self):
        return self._models

    def getCollection(self, name: str):
        return self._collections.get(name)

    def findItem(self, collectionName: str, itemId: str) -> ResultT:
        coll: Collection = self._collections.get(collectionName)
        if (coll):
            return coll.findById(itemId)
        return None

    def createItem(self, collectionName: str, item) -> ResultT:
        coll: Collection = self._collections.get(collectionName)
        if (coll):
            return coll.create(item)
        return None

    def deleteItem(self, collectionName: str, itemId: str) -> ResultT:
        coll: Collection = self._collections.get(collectionName)
        if (coll):
            return coll.deleteById(itemId)
        return None

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def save(self): pass
