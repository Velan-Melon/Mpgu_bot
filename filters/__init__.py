from aiogram import Dispatcher

from .privat_chat import IsPrivat

from .student import IsStudent
from .user import IsUser
from .abiturient import IsAbiturient
from .admin import IsAdmin
from .active import IsNotActive


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivat)
    dp.filters_factory.bind(IsStudent)
    dp.filters_factory.bind(IsUser)
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsNotActive)
    dp.filters_factory.bind(IsAbiturient)


