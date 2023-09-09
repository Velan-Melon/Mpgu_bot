#Сюда обязательно нужно импортировать все новые хендлеры для их последущей работы, хендлер error должен быть последний
from .start import dp
from .help import dp
from .profile import dp
from .hello import dp
from .begin_but import dp
from handlers.student.register import dp
from .game import dp
from handlers.student.timing import dp




__all__ = ['dp']