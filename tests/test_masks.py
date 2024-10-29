from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(numbers_cards):
    for number_card, result in numbers_cards:
        assert get_mask_card_number(number_card) == result


def test_get_mask_account(accounts):
    for account, result in accounts:
        assert get_mask_account(account) == result