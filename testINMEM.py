from db.Provider import Provider
from models.User import User
from models.Hotel import Hotel
from models.Route import Route
from models.Waybill import Waybill

provider = Provider()

u1 = User('Иванович', 'Иван', 'Иванов', 'г. Москва, ул. Ленина, д 123, кв 10', '9169761398', '1')
u2 = User('Поручникова', 'Юлия', 'Владимировна', 'г. Санкт-Петербург, ул. Маркса, д 24, кв 30', '9057525924', '2')
u3 = User('Жирнов', 'Евгений', 'Борисович', 'г. Томск, ул. Октябрьская, д 7, кв 17', '9169284356', '3')
provider.appendItem('User', u1)
provider.appendItem('User', u2)
provider.appendItem('User', u3)

h1 = Hotel('Сокол', 6300, 'Россия, Крым', '4')
h2 = Hotel('Саванна', 7000, 'США, Джорджия', '5')
h3 = Hotel('Джунгли', 5600, 'Индия, Нью-Дели', '6')
provider.appendItem('Hotel', h1)
provider.appendItem('Hotel', h2)
provider.appendItem('Hotel', h3)

r1 = Route('Жаркий Крым', 2, 'Умеренно-континентальный', h1, '7')
r2 = Route('Дикая Саванна', 4, 'Субэкваториальный', h2, '8')
r3 = Route('Индийские джунгли', 1, 'Субтропический', h3, '9')
r4 = Route('Русское Чёрное море', 4, 'Умеренно-континентальный', h1, '10')
provider.appendItem('Route', r1)
provider.appendItem('Route', r2)
provider.appendItem('Route', r3)
provider.appendItem('Route', r4)

w1 = Waybill(r4, u1, '20.06.2019', 3, '11')
w2 = Waybill(r2, u3, '03.10.2019', 1, '12')
w3 = Waybill(r3, u3, '10.04.2019', 2, '13')
provider.appendItem('Waybill', w1)
provider.appendItem('Waybill', w2)
provider.appendItem('Waybill', w3)

# Вывод эл-тов из всех коллекций
print(provider)
# Проверка рассчёта суммы для путёвки
print(w1.getCost() == 17955.0)
print(w2.getCost() == 7000)
print(w3.getCost() == 10640.0)

w1 = provider.findItem('Waybill', w1.getId())
w2 = provider.findItem('Waybill', w2.getId())
w3 = provider.findItem('Waybill', w3.getId())

# Вывод эл-тов из всех коллекций
print(provider)
# Проверка рассчёта суммы для путёвки
print(w1.getCost() == 17955.0)
print(w2.getCost() == 7000)
print(w3.getCost() == 10640.0)

provider.removeItem('Waybill', w3.getId())
provider.removeItem('Route', r3.getId())
provider.removeItem('User', u3.getId())


# Вывод эл-тов из всех коллекций
print(provider)
