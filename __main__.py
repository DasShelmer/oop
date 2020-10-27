from db.JSONProvider import JSONProvider

json = JSONProvider("db.json", "out.json")
json.load()
json.save()
