from db.Document import Document


class Waybill(Document):
    def __init__(self, collection, routeID='', userID='', departureDate='', count=0.0, raw={}):
        self._routeID = routeID
        self._userID = userID
        self._departureDate = departureDate
        self._count = count
        super().__init__(collection=collection, raw=raw)

    @property
    def routeID(self):
        return self._routeID

    @routeID.setter
    def routeID(self, routeID):
        self._routeID = routeID

    @property
    def userID(self):
        return self._userID

    @userID.setter
    def userID(self, userID):
        self._userID = userID

    @property
    def departureDate(self):
        return self._departureDate

    @departureDate.setter
    def departureDate(self, departureDate):
        self._departureDate = departureDate

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    def getUser(self):
        return self._provider.findItem('User', self._userID)

    def getRoute(self):
        return self._provider.findItem('Route', self._routeID)

    @property
    def discount(self):
        return 5 if self._count > 1 else 0

    def getCost(self):
        route = self.getRoute()
        if not route:
            raise TypeError('Bad RouteID')
        hotel = route.getHotel()
        if not hotel:
            raise TypeError('Bad HotelID')
        fullCost = hotel.cost * self.count
        discount = self.discount
        return fullCost * (1 - discount / 100) if discount else fullCost
