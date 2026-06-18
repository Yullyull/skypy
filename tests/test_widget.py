import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
    ],
)
def test_mask_account_card(account_info: str, expected: str) -> None:
    assert mask_account_card(account_info) == expected


@pytest.mark.parametrize(
    "account_info, expected",
    [
        ("", ""),
        ("ТолькоСлово", "ТолькоСлово"),
    ],
)
def test_mask_account_card_invalid(account_info: str, expected: str) -> None:
    assert mask_account_card(account_info) == expected


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-01-01T00:00:00.000000", "01.01.2018"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected
