from db.Document import Document
from typing import TypeVar


class User(Document):
    def __init__(self, collection, secname='', firstname='', patronym='', adress='', phone='', raw={}):
        self._secname = secname
        self._firstname = firstname
        self._patronym = patronym
        self._adress = adress
        self._phone = phone
        super().__init__(collection=collection, raw=raw)

    @property
    def secname(self):
        return self._secname

    @secname.setter
    def secname(self, secname):
        self._secname = secname

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def patronym(self):
        return self._patronym

    @patronym.setter
    def patronym(self, patronym):
        self._patronym = patronym

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, adress):
        self._adress = adress

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone


TUser = TypeVar('TUser', bound=User)
