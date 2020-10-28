from typing import List, TypeVar, Optional, Dict, TYPE_CHECKING
if TYPE_CHECKING:
    from .Provider import TProvider
from .Document import TDocument


class Collection():
    _items: Dict[str, TDocument]
    _itemClass: TDocument
    _provider: 'TProvider'
    _name: str

    def __init__(self, provider: 'TProvider', name: str, items: List[Dict[str, TDocument]]):
        self._provider = provider
        self._name = name
        self._itemClass = next((model for model in provider.models if model.__name__ == name))
        itemsRaw = list(self._itemClass(collection=self, raw=item) for item in items)
        self._items = dict(map((lambda item: (item.id, item)), itemsRaw))

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    @property
    def provider(self):
        return self._provider

    def findById(self, id: str) -> Optional[TDocument]:
        return self._items.get(id)

    def deleteById(self, id: str) -> Optional[TDocument]:
        return self._items.pop(id)

    def create(self, item: TDocument):
        self._items[item.id] = item
        return item

    def __eq__(self, other):
        return self._name == other._name

    def getItemsList(self) -> List[TDocument]:
        return list(dict(self._items[itemId]) for itemId in self._items)


TCollection = TypeVar('TCollection', bound=Collection)
