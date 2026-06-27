# Bank Widget

Бэкенд для виджета последних банковских операций клиента. Проект содержит
функции для маскировки номеров карт и счетов, форматирования виджета операций,
а также фильтрации и сортировки списка операций.

## Технологии

- **Python** 3.10+
- **Poetry** — управление зависимостями
- **pytest** + **pytest-cov** — тестирование
- **flake8**, **black**, **isort** — линтинг и форматирование
- **mypy** — статическая типизация

## Установка

Убедитесь, что установлен [Poetry](https://python-poetry.org/).

```bash
# Клонировать репозиторий
git clone https://github.com/Yullyull/skypy.git
cd skypy

# Установить зависимости (включая инструменты линтинга)
poetry install --with lint
```

## Использование

Активируйте виртуальное окружение:

```bash
poetry shell
# или одной командой:
poetry run python -c "from src.masks import get_mask_card_number; print(get_mask_card_number('7000792289606361'))"
```

### Модули

#### `src.masks` — маскировка номеров

```python
from src.masks import get_mask_card_number, get_mask_account

# Маскировка номера карты (16 цифр)
get_mask_card_number("7000792289606361")  # "7000 79** **** 6361"

# Маскировка номера счёта
get_mask_account("73654108430135874305")  # "**4305"
```

#### `src.widget` — виджет операций

```python
from src.widget import mask_account_card, get_date

# Маскировка карты с названием
mask_account_card("Visa Platinum 7000792289606361")
# "Visa Platinum 7000 79** **** 6361"

# Маскировка счёта с названием
mask_account_card("Счет 73654108430135874305")
# "Счет **4305"

# Преобразование ISO-даты в ДД.ММ.ГГГГ
get_date("2024-03-11T02:26:18.671407")
# "11.03.2024"
```

#### `src.processing` — обработка списка операций

```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]

# Фильтрация по статусу (по умолчанию EXECUTED)
filter_by_state(operations)
filter_by_state(operations, "CANCELED")

# Сортировка по дате (по умолчанию — убывание, сначала новые)
sort_by_date(operations)
sort_by_date(operations, reverse=False)
```

## Тестирование

```bash
# Запуск всех тестов
poetry run pytest

# С отчётом о покрытии
poetry run pytest --cov=src --cov-report=term-missing
```

## Линтинг и форматирование

```bash
# Проверка стиля
poetry run flake8 src/ tests/

# Проверка типов
poetry run mypy src/ tests/

# Автоформатирование
poetry run black src/ tests/
poetry run isort src/ tests/
```

## Структура проекта

```
skypy/
├── src/
│   ├── __init__.py
│   ├── masks.py           # Маскировка номеров карт и счетов
│   ├── processing.py      # Фильтрация и сортировка операций
│   └── widget.py          # Виджет форматирования операций
├── tests/
│   ├── __init__.py
│   ├── test_masks.py      # Тесты маскировки
│   ├── test_processing.py # Тесты фильтрации и сортировки
│   └── test_widget.py     # Тесты виджета
├── pyproject.toml         # Конфигурация проекта и зависимостей
└── README.md
```
