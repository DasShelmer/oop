from db.Document import Document


class Waybill(Document):
    def __init__(self, collection, route='', user='', departureDate='', count=0.0, raw={}):
        self._route = route
        self._user = user
        self._departureDate = departureDate
        self._count = count
        super().__init__(collection=collection, raw=raw)

    @property
    def route(self):
        return self._provider.findItem('Route', self._route)

    @route.setter
    def route(self, route):
        self._route = route._id

    @property
    def user(self):
        return self._provider.findItem('User', self._user)

    @user.setter
    def user(self, user):
        self._user = user._id

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

    @property
    def discount(self):
        return 5 if self._count > 1 else 0

    @property
    def cost(self):
        fullCost = self.route.cost * self.count
        return fullCost * (1 - self.discount / 100) if self.discount else fullCost
