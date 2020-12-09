from .Route import Route
from .User import User
from .Waybill import Waybill
from .Hotel import Hotel

# Модели док-ов для работы системы сохранения-загрузки
# и определения кол-ва коллекций у провайдеров.
models = [User, Hotel, Route, Waybill]
