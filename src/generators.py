from collections.abc import Iterator
from typing import Any


def filter_by_currency(
    transactions: list[dict[str, Any]], currency: str = "USD"
) -> Iterator[dict[str, Any]]:
    """Возвращает итератор транзакций с заданной валютой.

    Args:
        transactions: Список словарей с данными транзакций.
        currency: Код валюты для фильтрации (по умолчанию "USD").

    Yields:
        Словарь транзакции, если её валюта совпадает с запрошенной.
    """
    for t in transactions:
        code = t.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency:
            yield t


def transaction_descriptions(
    transactions: list[dict[str, Any]]
) -> Iterator[str]:
    """Возвращает описание каждой транзакции по очереди.

    Args:
        transactions: Список словарей с данными транзакций.

    Yields:
        Строка с описанием транзакции.
    """
    for t in transactions:
        yield t.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: Начальное значение диапазона.
        stop: Конечное значение диапазона.

    Yields:
        Номер карты в формате "XXXX XXXX XXXX XXXX".
    """
    for num in range(start, stop + 1):
        digits = f"{num:016d}"
        yield f"{digits[:4]} {digits[4:8]} {digits[8:12]} {digits[12:]}"
