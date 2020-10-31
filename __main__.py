from db.JSONProvider import JSONProvider
from models.User import User

json = JSONProvider("db.json", "out.json")
json.load()

u1 = User(None, 'Zubenko', 'Vasilii', 'Petrovich')
json.createItem('User', u1)

json.save()
