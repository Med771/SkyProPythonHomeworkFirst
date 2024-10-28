from time import strftime, strptime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Принимает информацию о карте типа str в форматах Card Type Number / Account Number.
    В зависимости от ответа, возвращает str в форматах Card Type .... ..** **** .... / Account **...."""

    info_values = card_info.split()

    if len(info_values) == 3:
        return f"{info_values[0]} {info_values[1]} {get_mask_card_number(info_values[2])}"

    if len(info_values) == 2:
        return f"{info_values[0]} {get_mask_account(info_values[1])}"

    return ""


def get_date(date: str) -> str:
    """Принимает дату типа str в формате%Y-%m-%dT%H:%M:%S.%f.
    Возвращает дату типа str в формате %d.%m.%Y."""
    if not isinstance(date, str):
        return "Date type incorrect"

    date.strip()

    try:
        reformatted = strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return "Date format incorrect"

    return strftime("%d.%m.%Y", reformatted)


if __name__ == "__main__":
    data_info_cards = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]

    for card in data_info_cards:
        print(mask_account_card(card_info=card))
