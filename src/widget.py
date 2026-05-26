from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Маскирует номер карты или счёта."""
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
    """Возвращает дату в формате ДД.ММ.ГГГГ."""
    return datetime.fromisoformat(date_string).strftime("%d.%m.%Y")
