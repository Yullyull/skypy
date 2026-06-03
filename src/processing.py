from typing import Any


def filter_by_state(
    data: list[dict[str, Any]], state: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Фильтрует список словарей по значению ключа state."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, Any]], reverse: bool = True
) -> list[dict[str, Any]]:
    """Сортирует список словарей по ключу date."""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
