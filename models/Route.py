from db.Document import Document
from typing import TypeVar, Optional
from .Hotel import THotel


class Route(Document):
    def __init__(self, collection, duration=0.0, hotel='', raw={}):
        self._duration = duration
        self._hotel = hotel
        super().__init__(collection=collection, raw=raw)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def hotel(self):
        return self._hotel

    @hotel.setter
    def hotel(self, hotel):
        self._hotel = hotel

    @property
    def cost(self):
        return self.hotel.cost

    def getHotel(self) -> Optional[THotel]:
        return self._provider.findItem('Hotel', self._hotel)


TRoute = TypeVar('TRoute', bound=Route)
