# Bank Widget

Бэкенд для виджета последних банковских операций клиента.

## Установка

```bash
poetry install --with lint
```

## Модули

### `src/masks` — маскировка номеров

```python
from src.masks import get_mask_card_number, get_mask_account

get_mask_card_number("7000792289606361")  # "7000 79** **** 6361"
get_mask_account("73654108430135874305")  # "**4305"
```

### `src/widget` — виджет операций

```python
from src.widget import mask_account_card, get_date

mask_account_card("Visa Platinum 7000792289606361")  # "Visa Platinum 7000 79** **** 6361"
mask_account_card("Счет 73654108430135874305")        # "Счет **4305"
get_date("2024-03-11T02:26:18.671407")               # "11.03.2024"
```

### `src/processing` — обработка списка операций

```python
from src.processing import filter_by_state, sort_by_date

# Фильтрация по статусу (по умолчанию EXECUTED)
filter_by_state(operations)
filter_by_state(operations, "CANCELED")

# Сортировка по дате (по умолчанию убывание)
sort_by_date(operations)
sort_by_date(operations, reverse=False)
```

## Линтинг

```bash
poetry run black src/
poetry run isort src/
poetry run flake8 src/
poetry run mypy src/
```
