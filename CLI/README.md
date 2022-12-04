# Как воспользоваться

## Предварительная настройка:

- Пишем команду в директории проекта для создания виртуального окружения:

    ```
    python -m venv venv
    ```

- Активируем виртуальное окружение:

    - для Windows
        ```
        venv\Scripts\activate.bat
        ```
    - для Linux и MacOS
        ```
        source venv/bin/activate
        ```

- Скачиваем все необходимые пакеты:

    ```
    pip install -r CLI/requirements.txt
    ```

- Скачиваем [bert_punctuation.tar.gz](https://drive.google.com/file/d/1-1kCt3pn0CyRf-e_nBVyD1g3yK7mN1rc/view?usp=share_link) и [vocab.txt](https://drive.google.com/file/d/1wm6AnoX4aVVXmaWajj1bb5qDWp3Fjr3P/view?usp=share_link), переносим оба файла в `CLI/core/preprocessing/logical_parts/Bert_Russian_punctuation/`

- Скачиваем [model.pth](https://drive.google.com/file/d/1k-Bp7Obr7mPVdikzyYSkNwkJPYle-fyH/view?usp=share_link), переносим файл в `CLI/core/sentiment_analysis_models/rubert_base_cased/model_data/`

- Запускаем скрипт `CLI/model_getter.py`

## Описание функций

### Служебные классы

> В файле `CLI/core/commons.py` содержаться следующие классы:

- `Sentiment`(Enum) - [NEUTRAL, POSITIVE, NEGATIVE]
- `_Processed_text`(object) - Обертка над обработанным текстом
- `_Dataset_processed_texts`(object) - Обертка над обработанным корпусом текстов

### Обрабатывающие функции

> В файле `CLI/core/processing_functions.py` доступны следующие функции:

- `processing_text`(text, object_review_size) - Анализ тональности текста
- `processing_formatted_text`(text, object_review_size) - Форматирование и анализ тональности текста
- `processing_logical_parts`(text, object_review_size) - Разбиение на логические части, форматирование и анализ тональности текста
- `processing_dataset`(input_path, size, object_review_size) - Анализ тональности корпуса текстов
- `processing_formatted_dataset`(input_path, size, object_review_size) - Форматирование и анализ тональности корпуса текстов
- `processing_logical_parts_dataset`(input_path, size, object_review_size) - Разбиение на логические части, форматирование и анализ тональности корпуса текстов
- `save_dataset`(dataset, output_path) - Сохранение обработанного корпуса текстов

### Статистические функции

> В файле `CLI/core/statistics_functions.py` доступны следующие функции:

- `get_processed_texts`(path) - Загрузка корпуса обработанных текстов
- `get_pos_processed_texts`(dataset) - Извлечение позитивных текстов из набора данных
- `get_neg_processed_texts`(dataset) - Извлечение негативных текстов из набора данных
- `get_neu_processed_texts`(dataset) - Извлечение нейтральных текстов из набора данных
- `frequency_str`(ngrams) - Подсчет частоты n-грамм
- `get_ngram`(dataset_processed_texts, n) - Извлечение n-грамм из корпуска обработанных текстов
- `get_norm_ngram`(dataset_processed_texts, n) - Извлечение и нормализация n-грамм из корпуска обработанных текстов
- `save_frequency_str`(frequency_str, save_path) - Сохранение частоты n-грамм

## Анализ текста из скрипта:

В файле `CLI/test.py` можно вызвать функцию `text_tonality`, которая принимает 3 аргумента:

- `input_text`: str - Исходный текст
- `preprocessing`: _Preprocessing(Enum):
    - `WITHOUT_PREPROCESSING` - Анализ исходного текста
    - `TEXT_FORMATTING` - Форматирование текста
    - `LOGICAL_PARTS` - Форматирование и разбиение на логические части
- `object_review_size`: int = 5 - Количество слов в объекте отзыва

В консоле будет результат: тональность и объект отзыва 

## CLI

...

## Статистика 

В файле `CLI/statistics.py` можно вызвать функцию `frequency_ngrams`, которая принимает 5 аргументов:

- `input_path`: str - Путь до обработанного корпуса
- `output_path`: str - Путь, где будет сохранен результат
- `sentiment`: Sentiment(Enum) - Выбор тональности
- `n`: int - Размер n-грамм
- `normalization`: bool = True - Использование нормализации слов

Функция подсчитывает частоту n-грамм среди всех объектов отзыва в корпусе текстов