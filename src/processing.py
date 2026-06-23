from typing import Any


def filter_by_state(
    data: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Фильтрует список словарей по значению ключа state.

    Возвращает только те элементы, у которых значение ключа "state"
    совпадает с переданным значением.

    Args:
        data: Список словарей с данными операций.
        state: Статус для фильтрации (по умолчанию "EXECUTED").

    Returns:
        Отфильтрованный список словарей.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """Сортирует список словарей по ключу date.

    Args:
        data: Список словарей с данными операций.
        reverse: Если True — сортировка по убыванию (сначала новые),
                 если False — по возрастанию (сначала старые).

    Returns:
        Отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
