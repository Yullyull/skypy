# Bank Widget Backend

Backend data preparation for a bank client's operations widget.

## Project Structure

```
bank_widget/
├── src/
│   ├── __init__.py
│   ├── masks.py    # Card and account masking functions
│   └── widget.py   # Widget helper functions
├── tests/
│   └── __init__.py
├── .flake8
├── .gitignore
└── pyproject.toml
```

## Modules

### `src/masks`
- `get_mask_card_number(card_number)` — masks a 16-digit card as `XXXX XX** **** XXXX`
- `get_mask_account(account_number)` — masks an account number as `**XXXX`

### `src/widget`
- `mask_account_card(account_info)` — accepts a combined string like
  `"Visa Platinum 7000792289606361"` or `"Счет 73654108430135874305"`
  and returns it with a masked number
- `get_date(date_string)` — converts `"2024-03-11T02:26:18.671407"` → `"11.03.2024"`

## Setup

```bash
poetry install --with lint
```

## Linting

```bash
poetry run black src/ tests/
poetry run isort src/ tests/
poetry run flake8 src/ tests/
poetry run mypy src/
```
