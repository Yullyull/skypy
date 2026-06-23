from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations() -> list[dict[str, Any]]:
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("PENDING", []),
    ],
)
def test_filter_by_state(
    operations: list[dict[str, Any]], state: str, expected_ids: list[int]
) -> None:
    result = filter_by_state(operations, state)
    assert [op["id"] for op in result] == expected_ids


def test_filter_by_state_default(operations: list[dict[str, Any]]) -> None:
    result = filter_by_state(operations)
    assert all(op["state"] == "EXECUTED" for op in result)
    assert len(result) == 2


def test_filter_by_state_empty() -> None:
    assert filter_by_state([]) == []


@pytest.mark.parametrize(
    "reverse, expected_first_id",
    [
        (True, 41428829),
        (False, 939719570),
    ],
)
def test_sort_by_date(
    operations: list[dict[str, Any]], reverse: bool, expected_first_id: int
) -> None:
    result = sort_by_date(operations, reverse=reverse)
    assert result[0]["id"] == expected_first_id


def test_sort_by_date_default(operations: list[dict[str, Any]]) -> None:
    result = sort_by_date(operations)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)
