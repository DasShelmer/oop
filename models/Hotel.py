from db.Document import Document
from typing import TypeVar


class Hotel(Document):
    def __init__(self, collection, name='', cost=0.0, country='', climate='', raw={}):
        self._name = name
        self._cost = cost
        self._country = country
        self._climate = climate
        super().__init__(collection=collection, raw=raw)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def climate(self):
        return self._climate

    @climate.setter
    def climate(self, climate):
        self._climate = climate


THotel = TypeVar('THotel', bound=Hotel)
