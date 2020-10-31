from models import models
from .Collection import Collection


class Provider():
    def __init__(self):
        self._models = models
        self._collections = {}
        for model in models:
            self._collections[model.__name__] = Collection(self, model.__name__, [])

    @property
    def models(self):
        return self._models

    def getCollection(self, name: str):
        return self._collections.get(name)

    def findItem(self, collectionName: str, itemId: str):
        coll = self._collections.get(collectionName)
        if (coll):
            return coll.findById(itemId)
        return None

    def createItem(self, collectionName: str, item):
        coll = self._collections.get(collectionName)
        if (coll):
            return coll.create(item)
        return None

    def deleteItem(self, collectionName: str, itemId: str):
        coll = self._collections.get(collectionName)
        if (coll):
            return coll.deleteById(itemId)
        return None

    def load(self): pass

    def save(self): pass
