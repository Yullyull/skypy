def get_mask_card_number(card_number: str) -> str:
    """Mask a bank card number.

    Takes a 16-digit card number and returns it masked in the format
    XXXX XX** **** XXXX, where first 6 and last 4 digits are visible.

    Args:
        card_number: A string of 16 digits representing the card number.

    Returns:
        Masked card number as a formatted string.
    """
    digits = card_number.replace(" ", "")
    masked = digits[:6] + "**" + "****" + digits[-4:]
    return f"{masked[0:4]} {masked[4:8]} {masked[8:12]} {masked[12:16]}"


def get_mask_account(account_number: str) -> str:
    """Mask a bank account number.

    Takes an account number and returns its mask showing only the last
    4 digits preceded by two asterisks: **XXXX.

    Args:
        account_number: A string of at least 4 digits representing the account.

    Returns:
        Masked account number as a string in the format **XXXX.
    """
    return f"**{account_number[-4:]}"
