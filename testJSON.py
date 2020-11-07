from db.JSONProvider import JSONProvider
from models.User import User
from models.Hotel import Hotel
from models.Route import Route
from models.Waybill import Waybill

jsonP = JSONProvider('', 'test.json')

u1 = User('Иванович', 'Иван', 'Иванов', 'г. Москва, ул. Ленина, д 123, кв 10', '9169761398', '1')
u2 = User('Поручникова', 'Юлия', 'Владимировна', 'г. Санкт-Петербург, ул. Маркса, д 24, кв 30', '9057525924', '2')
u3 = User('Жирнов', 'Евгений', 'Борисович', 'г. Томск, ул. Октябрьская, д 7, кв 17', '9169284356', '3')
jsonP.appendItem('User', u1)
jsonP.appendItem('User', u2)
jsonP.appendItem('User', u3)

h1 = Hotel('Сокол', 6300, 'Россия, Крым', '4')
h2 = Hotel('Саванна', 7000, 'США, Джорджия', '5')
h3 = Hotel('Джунгли', 5600, 'Индия, Нью-Дели', '6')
jsonP.appendItem('Hotel', h1)
jsonP.appendItem('Hotel', h2)
jsonP.appendItem('Hotel', h3)

r1 = Route('Жаркий Крым', 2, 'Умеренно-континентальный', h1, '7')
r2 = Route('Дикая Саванна', 4, 'Субэкваториальный', h2, '8')
r3 = Route('Индийские джунгли', 1, 'Субтропический', h3, '9')
r4 = Route('Русское Чёрное море', 4, 'Умеренно-континентальный', h1, '10')
jsonP.appendItem('Route', r1)
jsonP.appendItem('Route', r2)
jsonP.appendItem('Route', r3)
jsonP.appendItem('Route', r4)

w1 = Waybill(r4, u1, '20.06.2019', 3, '11')
w2 = Waybill(r2, u3, '03.10.2019', 1, '12')
w3 = Waybill(r3, u3, '10.04.2019', 2, '13')
jsonP.appendItem('Waybill', w1)
jsonP.appendItem('Waybill', w2)
jsonP.appendItem('Waybill', w3)

print(jsonP)
print(w1.getCost() == 17955.0)
print(w2.getCost() == 7000)
print(w3.getCost() == 10640.0)

jsonP.save()
del jsonP

jsonP = JSONProvider('test.json', 'test.json')
jsonP.load()
w1 = jsonP.findItem('Waybill', w1.getId())
w2 = jsonP.findItem('Waybill', w2.getId())
w3 = jsonP.findItem('Waybill', w3.getId())

print(jsonP)
print(w1.getCost() == 17955.0)
print(w2.getCost() == 7000)
print(w3.getCost() == 10640.0)

jsonP.removeItem('Waybill', w3.getId())
jsonP.removeItem('Route', r3.getId())
jsonP.removeItem('User', u3.getId())


print(jsonP)
jsonP.save()
