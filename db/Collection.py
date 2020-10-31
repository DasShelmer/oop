
class Collection():

    def __init__(self, provider, name, items):
        self._provider = provider
        self._name = name
        for model in provider.models:
            if model.__name__ == name:
                self._itemClass = model
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

    def findById(self, id: str):
        return self._items.get(id)

    def deleteById(self, id: str):
        return self._items.pop(id)

    def create(self, item):
        item.collection = self
        self._items[item.id] = item

        return item

    def __eq__(self, other):
        return self._name == other._name

    def getItemsList(self):
        return list(dict(self._items[itemId]) for itemId in self._items)
