from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#это инлайн кнопки которые будут появляться с сообщениями
ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        #callback_data это данные которые мы получаем с нажатия кнопки, а url ссылка на которую переправляет кнопка
                                        InlineKeyboardButton(text="Тудым", callback_data="Сюдым"),
                                        InlineKeyboardButton(text="В Сибирь", url="https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fkirov-portal.ru%2Fupload%2Fresize_cache%2Fsite_news_detail_1%2F1280_768_0%2F343%2F343c7514834d53148437b2ca22b851ec.jpg&lr=36&pos=0&rpt=simage&text=сибирь")
                                    ],
                                    [
                                        InlineKeyboardButton(text="ooooooooooo", callback_data="Че рот открыл?")
                                    ],
                                    [
                                        InlineKeyboardButton(text="Давай, нажми и убей меня!", callback_data="замена ин 1")
                                    ]
                                ])