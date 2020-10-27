from .Provider import Provider
from .Collection import Collection
import json
import os

__dir__ = os.path.dirname(os.path.realpath('__file__')) + "\\"


class JSONProvider(Provider):
    def __init__(self, readFile: str, writeFile: str):
        self._readFile = readFile
        self._writeFile = writeFile
        super().__init__()

    def load(self):
        f = open(__dir__ + self._readFile, 'r')
        raw = json.load(f)
        f.close()
        self._collections = dict((collName, Collection(self, collName, raw[collName])) for collName in raw)

    def save(self):
        resJson = dict((collName, self._collections[collName].getItemsList()) for collName in self._collections)
        f = open(os.path.join(__dir__ + self._writeFile), 'w')
        json.dump(resJson, f, sort_keys=True, indent=4)
        f.close()
