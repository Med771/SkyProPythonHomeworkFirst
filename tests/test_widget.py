from src.widget import get_date, mask_account_card


def test_get_date(dates: list[tuple]) -> None:
    for date, result in dates:
        assert get_date(date) == result


def test_mask_account_card(accounts_cards: list[tuple]) -> None:
    for query, result in accounts_cards:
        assert mask_account_card(query) == result
