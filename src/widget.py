from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Маскирует номер карты или счёта.

    Принимает строку вида "Visa Platinum 7000792289606361" или
    "Счет 73654108430135874305" и возвращает замаскированный номер.

    Args:
        account_info: Строка с названием и номером карты/счёта.

    Returns:
        Строка с замаскированным номером.
    """
    if not account_info:
        return ""
    parts = account_info.rsplit(" ", 1)
    if len(parts) < 2:
        return account_info
    label, number = parts
    if label.lower() == "счет":
        return f"{label} {get_mask_account(number)}"
    return f"{label} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Преобразует ISO-дату в формат ДД.ММ.ГГГГ.

    Args:
        date_string: Строка с датой в ISO-формате
                     (например, "2024-03-11T02:26:18.671407").

    Returns:
        Отформатированная дата (например, "11.03.2024").
    """
    return datetime.fromisoformat(date_string).strftime("%d.%m.%Y")
