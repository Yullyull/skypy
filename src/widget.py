from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Mask a bank card or account number from a combined info string.

    Accepts a string containing the card/account type followed by its number.
    Applies the appropriate masking depending on whether the entry is an
    account (keyword 'Счет') or a card.

    Args:
        account_info: A string like 'Visa Platinum 7000792289606361'
                      or 'Счет 73654108430135874305'.

    Returns:
        The original type label with the masked number appended.

    Examples:
        >>> mask_account_card('Visa Platinum 7000792289606361')
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card('Счет 73654108430135874305')
        'Счет **4305'
    """
    parts = account_info.rsplit(" ", 1)
    label = parts[0]
    number = parts[1]

    if label.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{label} {masked_number}"


def get_date(date_string: str) -> str:
    """Convert an ISO 8601 datetime string to DD.MM.YYYY format.

    Args:
        date_string: A datetime string like '2024-03-11T02:26:18.671407'.

    Returns:
        A date string formatted as 'DD.MM.YYYY', e.g. '11.03.2024'.

    Examples:
        >>> get_date('2024-03-11T02:26:18.671407')
        '11.03.2024'
    """
    date_part = date_string[:10]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
