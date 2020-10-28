from db.Document import Document
from typing import Optional
from .Route import TRoute
from .User import TUser


class Waybill(Document):
    def __init__(self, collection, route='', user='', departureDate='', count=0.0, raw={}):
        self._route = route
        self._user = user
        self._departureDate = departureDate
        self._count = count
        super().__init__(collection=collection, raw=raw)

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, route):
        self._route = route

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

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

    def getUser(self) -> Optional[TUser]:
        return self._provider.findItem('User', self._user)

    def getRoute(self) -> Optional[TRoute]:
        return self._provider.findItem('Route', self._route)

    def getDiscount(self):
        return 5 if self._count > 1 else 0

    def getCost(self):
        route = self.getRoute()
        if not route:
            raise TypeError('Bad Route by id %s', self._route)
        fullCost = route.cost * self.count
        discount = self.getDiscount()
        return fullCost * (1 - discount / 100) if discount else fullCost
