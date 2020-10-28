import time
import struct
from typing import List, TypeVar, TYPE_CHECKING
if TYPE_CHECKING:
    from .Provider import TProvider
    from .Collection import TCollection


class Document:
    _id: str
    _propsToSave: List[str]
    _collection: 'TCollection'
    _provider: 'TProvider'

    def __init__(self, collection: 'TCollection', raw={}):
        self._collection = collection
        self._provider = collection.provider

        if '_id' in raw:
            self._id = raw['_id']
        else:
            self._id = Document._generateId()

        all_props = dir(self)
        self._propsToSave = list(name for name in all_props if name.startswith('_') and name[1:] in all_props)

        for name in self._propsToSave:
            if name in raw:
                setattr(self, name, raw[name])

    @property
    def id(self):
        return self._id

    def __eq__(self, other):
        return self._id == other._id

    def __hash__(self):
        return self._id

    def __iter__(self):
        for key in self._propsToSave:
            yield (key, getattr(self, key))

    @staticmethod
    def _generateId():
        return struct.pack('f', time.time()).hex()


TDocument = TypeVar('TDocument', bound=Document)
