from db.Document import Document


class Route(Document):
    def __init__(self, collection, duration=0.0, climate='', hotelID='', raw={}):
        self._duration = duration
        self._hotelID = hotelID
        self._climate = climate
        super().__init__(collection=collection, raw=raw)

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = duration

    @property
    def hotelID(self):
        return self._hotelID

    @hotelID.setter
    def hotelID(self, hotelID):
        self._hotelID = hotelID

    @property
    def climate(self):
        return self._climate

    @climate.setter
    def climate(self, climate):
        self._climate = climate

    def getHotel(self):
        return self._provider.findItem('Hotel', self._hotelID)
