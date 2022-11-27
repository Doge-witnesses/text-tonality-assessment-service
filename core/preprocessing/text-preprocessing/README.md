**Для использования необходимо установить: !pip install pyxDamerauLevenshtein**



**Функция fix_command():**

>Вход: Слово (токен) : str, Словарь : list[str]

>Выход: Слово с исправленной орфографией : str

Под словарем подразумевается именно list-type объект.

**Функция text_ru_clear():**

>Вход: Текст : str

>Выход: Текст, состоящий только из символов кириллицы : str



**Функция text_preprocessing():**

>Вход: Текст : str,  Словарь : list[str]

>Выход: Форматированный текст : str

По сути, совмещает в себе text_ru_clear() и fix_command().



**Функция tokenization():**

>Вход: Форматированный текст (результат функции text_preprocessing()) : str

>Выход: Список слов (токенов) : list[str]



Пример:

text = "Некатырый текс!?"

text = tokenization(text_preprocessing(text, dictionary))

print(text) # ['некоторый', 'текст']
